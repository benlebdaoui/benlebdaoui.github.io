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
[Redirect Head to Head Stats Dataset](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/jupyter/head_to_head_stats.xls)  
[Redirect Team Stats dataset](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/jupyter/premier_league_2023_24.xls)  

Feb 14, 2025: I fixed the problem by lowering the coefficient of the home advantage to 0.2 and increasing the coefficients for head to head stats and goals conceded. Now all of the predictions that the model makes are pretty accurate, and now I'm working on the front-end site.  
[Example Prediction](https://raw.githubusercontent.com/benlebdaoui/benlebdaoui.github.io/main/assets/jupyter/test_model.ipynb) 

March 2, 2025: I took some time to touch up on HTML and learn enough JavaScript to create a very basic interface to run the model. It is now completely working and uploaded to my GitHub as its own repo! You can use [this link](https://github.com/benlebdaoui/prem_predictor) to navigate to it to check out all the code as well as the datasets I created.

March 19, 2025: I found some datasets from the 2021/22 and 2022/23 seasons, cleaned those, and then concatonated them with the original dataset. I also retrained the model without taking possession as a feature and it changed nothing so I took it out completely. I retrained the model on all three datasets together and the accuracy on the test set improved from 80.26% to 92.11%. The new changes have been pushed to the project repo.

