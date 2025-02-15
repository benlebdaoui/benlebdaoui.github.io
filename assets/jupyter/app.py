from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("match_predictor.pkl")

# Load team statistics & head-to-head stats
team_stats = pd.read_csv("premier_league_2023_24.csv")
head_to_head = pd.read_csv("head_to_head_stats.csv")

# Ensure team names match exactly
team_stats["Team"] = team_stats["Team"].str.strip()
head_to_head["team"] = head_to_head["team"].str.strip()
head_to_head["opponent"] = head_to_head["opponent"].str.strip()

# Function to get a team's stats
def get_team_stats(team_name):
    row = team_stats[team_stats["Team"] == team_name]
    return row.iloc[0] if not row.empty else None

# Function to get head-to-head stats
def get_head_to_head(home_team, away_team):
    row = head_to_head[(head_to_head["team"] == home_team) & (head_to_head["opponent"] == away_team)]
    return row.iloc[0] if not row.empty else {"head_to_head": 0, "head_to_head_goals": 0}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input from request
        data = request.json
        home_team = data.get("home_team")
        away_team = data.get("away_team")

        # Validate inputs
        if not home_team or not away_team:
            return jsonify({"error": "Missing team names in request"}), 400

        # Retrieve stats
        home_stats = get_team_stats(home_team)
        away_stats = get_team_stats(away_team)
        h2h_stats = get_head_to_head(home_team, away_team)

        if home_stats is None or away_stats is None:
            return jsonify({"error": "Invalid team name"}), 400

        team_mapping = {team: idx + 1 for idx, team in enumerate(team_stats["Team"].unique())}
        opponent_encoded = team_mapping.get(away_team, 0) 
        # Prepare features for the model
        features = [
            float(home_stats["Recent Form"]), 
            float(home_stats["Avg Goals/Game"]), 
            float(home_stats["Avg Goals Against/Game"] * 3.0),
            float(home_stats["Avg Shots/Game"]), 
            float(home_stats["Avg Possession (%)"]),
            float(h2h_stats["head_to_head"] * 2.0), 
            float(h2h_stats["head_to_head_goals"] * 2.0), 
            opponent_encoded, 
            0.2,  # Home advantage (always 0.2)
        ]
        print("🔍 MODEL INPUT FEATURES:", features)
        # Make prediction
        prediction = model.predict([features])[0]

        # Convert numerical output to text
        result_mapping = {1: f"{home_team} wins", 0: "Draw", -1: f"{home_team} loses"}
        prediction_text = result_mapping.get(prediction, "Unknown")

        return jsonify({"home_team": home_team, "away_team": away_team, "prediction": prediction_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("✅ Flask is starting...")
    app.run(debug=True)



