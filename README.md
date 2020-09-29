### Football Scraping and Calculation tool

Personal project to get a deeper understanding of sports analytics, to leverage for story telling later on for lower-tier leagues. The repository is going to be broken down into the following sections, and their respective programs:

- **Calculators:** Contains the calculators used to do analysis on the scraped data files. 

  1. 'season_calcs.py' is a program that at this time simply recaps the team season-by-season data, and creates a summary of it from 2002-present. This includes all main captured data, as well as calculated over-90 calculations.

- **Prove_Outs:** Is just a folder for some example manual calculations for the over-90 metrics, and any other calculation prove-outs that are produced.

- **Scraping_Tool:** This folder contains the main scraping and parsing engines used for data gathering (specifically made for fbref.com). The programs gather, aggregate, parse, and output data to JSON files that are used to feed the calculation engine. Currently old parsing files are migrated and combined into one scraping engine running on a Jupyter Notebook - Once completed, a pure python file will be generated for ease of running in a GUI.

- **White_Papers:** Contains all white papers that are used as inspiration for the calculations, as well as some of which will be also used to produce some prove-outs of the models. This list of course isn't exhaustive, but is both the inspiration behing this, as well as the source of some further thought on the latter half of the build. For now these are rather far from full implementation.

### Currently building for the data parser:

**The Scraping engine is now considered feature complete - currently working on optimization on some slow loops:**

- [x] Adjusted for the scraping of the game list for a season.
- [x] Built parser to run through season automatically, instead of game-by-game via manual entry.
- [x] Built simple statistical inference for 'conceded' statistics.
- [ ] Full rebuild of Parsing engine on-going.

### Scraping Engine Optimizations:

- [ ] Add timing captures for process logging - needed for proper troubleshooting in optimization.
- [x] Increase the frequency of status indicators (for transparency, and speed analysis).
- [ ] Automate team list for calculating all teams at once for a season - currently all manual entry per-team.

### Currently building for the calculation engine:

- [ ] Calculate player performance throughout seasons (some stats are not shared on a player -level).
- [ ] Replicate FiveThirtyEight model for team success predictions.
- [ ] Apply some basic models (TBD) for team level analytics.

### Legend:

- **Calculation notation:** Goals (G), Assists (A), Penalties (PK), Shots on Target (SOT), Fouls (F), Cards (C), Per 90 Minutes (/90), Total Minutes Played (TM).

### Notes:

- Math for over 90s is simple, for example G+A-PK/90: ((G-PK)+A)/(TM/90). The float result effectively will define a simple performance metric to start with. Attached in the Proveouts folder is also a manual Prove_Out of some of the metrics, as fbref has them (Per90 Manual Prove Out.xlsx).
- All conceded statistics are based on opponent performance against the team. Shots conceded will be shots for the opposition, along with SOT being the shots on goal that were conceded.
- (SOT-Saves) should indicate the goals conceded as well - this will require some testing and data spot-checking, as there have been some instances where this hasn't been the case.

### Data Sources:
- https://www.github.com/jalapic/engsoccerdata
- https://www.fbref.com/
