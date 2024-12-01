# BSA Football Research Project 2024

How can a defense maximize their EPA in "clutch time"?

# [Introduction and Proposal](https://docs.google.com/presentation/d/17gTBEuxoZaykZ6PiA4hYioC999DcLKa3oJ7NxRFPB7o/edit?usp=sharing)

# Methodology

### Data Sources

Acquired from repos provided by nflverse. Here are the repo links for the types of dataframes:

- [play_by_play](https://github.com/nflverse/nflverse-data/releases/tag/pbp)
- [pbp_participation](https://github.com/nflverse/nflverse-data/releases/tag/pbp_participation)

Any data acquired from the GitHub links will be in the `data/raw` folder (not present in repo due to large size) while anything we cleaned/modified will be in the `dataClean/` directory. The data in the folder `refined` consists of data that was modfiied *after* being cleaned. In other words, the steps used to data pre-process is `raw -> cleanData -> refineData`.

### Packages Used in Conda
- pandas
- numpy
- matplotlib
- seaborn
- scikit
- os
- xgboost
- networkx
- streamlit
