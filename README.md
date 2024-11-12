# BSA Football Research Project 2024

How can a defense maximize their EPA in "clutch time"?

# [Introduction and Proposal](https://docs.google.com/presentation/d/17gTBEuxoZaykZ6PiA4hYioC999DcLKa3oJ7NxRFPB7o/edit?usp=sharing)

# Methodology

### Data Sources

Acquired from repos provided by nflverse. Here are the repo links for the types of dataframes:

- [play_by_play](https://github.com/nflverse/nflverse-data/releases/tag/pbp)
- [pbp_participation](https://github.com/nflverse/nflverse-data/releases/tag/pbp_participation)

Any data acquired from the GitHub links will be in the `data/raw` folder (not present in repo due to large size) while anything we cleaned/modified will be in the `dataClean/` directory.

### Packages Used in Conda
- pandas
- numpy
- matplotlib
- seaborn
- scikit
- os

## Features Used

- Quarter (4th)
- Time Left (2:00)
- Personnel
- Coverage
- Passing Splashes (Deep/Shallow, Left/Right/Middle)
- QB Aggression
- EPA
- Timeouts Left


## TODO:
### New Goal:
Now create model to predict probability of **route concepts** that will be called
  - In essence, we are now creating a classification model

#### Model Possibilties:
- Neural Networks
- Bayesian models
- Stochastic models
- Markov decision chain
- ARIMA
- Clustering
- T-distribution

### Eric
 - [ ] Continue to clean merged data
  - [ ] Merge highly similar personnel combos
- [ ] Add filters by team to see specific route concept tendencies
- [ ] See correlation between number of pass rushers vs time to throw
  - [ ] And see if I can also filter this information by QB clustering
- [ ] Markov decision chain

### Vardaan
- [ ] More exploratory data analysis
  - [ ] Check out different variables' correlation with EPA
  - [ ] Also examine multicollinearity
- [ ]

### Naren
- [ ] Look more into Bayesian approach
  - [ ] how to set up a model/classification for this situation
- [ ] Clustering models

### Aadrij
- [ ] QB quality (mobile vs pocket, good vs bad)
- [ ] ARIMA

### Nikhil
- [ ] Research Markov modeling and how it would apply to this project
- [ ] Markov

### Rithvik
- [ ] Markov
- [ ] ANOVA
