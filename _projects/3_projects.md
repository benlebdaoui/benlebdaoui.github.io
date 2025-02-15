---
layout: page
title: Premier League Match Predictor
description: 
img: assets/img/premlogo.jpg
importance: 3
category: work
related_publications: false
---

Feb 4, 2025: I am creating a simple ML model to predict results of premier league matches. I am using a dataset from Kaggle that consists of all the necessary information from the 2023/24 Premier League season. I'll start with a simple classification model that will predict win/loss/draw. If it works, I will try to sophisticate it to give a scoreline and incorporate data from many years.

Feb 9, 2025: I have finished cleaning and processing the data and creating the ML model. It works quite well, here is the code:  
[Download Premier League Match Predictor Code](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/pdf/premier_league_classification_predictor.pdf) 
The only issue is that it requires someone to input lots of information manually for the model to work. I am going to create a database with all of the necessary information for each team, and then a user-friendly website, so that someone can simply select and a home and away team from a dropdown, and that will automatically input all necessary information to the function.

Feb 13, 2025: I created the datasets necessary for automatic filling of the features required for the model, and then got those datasets connected to the model with Flask API. The model worked in a sense because it gave predictions, but there was such a strong bias for home teams that it never predicted a loss, even when inputting "home: Sheffield United" and "away: Manchester City" (the best team vs the worst team). I am now working on debugging that so it will predict losses as well as wins and draws.

Feb 14, 2025: I fixed the problem by lowering the coefficient of the home advantage to 0.2 and increasing the coefficients for head to head stats and goals conceded. I'll upload the datasets and app.py that Flask ran on and start working on the front-end site.  
[Redirect Head to Head Stats Dataset](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/jupyter/head_to_head_stats.xls)  
[Redirect Team Stats dataset](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/jupyter/premier_league_2023_24.xls)  
[Download app.py](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/juptyer/app.py) 
