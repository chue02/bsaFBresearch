# BSA Research Project

How can a defense maximize their EPA in "clutch time"?

# Methodology

## Data Sources

Provided by nflverse.
[Play-py-Play](https://github.com/nflverse/nflverse-data/releases/tag/pbp) data was acquired here while [NGS play-by-play](https://github.com/nflverse/nflverse-data/releases/tag/pbp_participation) data was acquired here.

Any data acquired from the GitHub links will be in the `data/raw` folder while anything we cleaned up will be in other folders of the `data` directory.

# TODO:

- [ ] Clean dataframes
- [ ] Figure out how to JOIN pbp and pbp_participation dataframes
  - Probably based on game id?
- [ ] Create zero-sum matrix using Tableau and EPA
  - [ ] Also create a way to paramterize this by year
