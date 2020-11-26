### Football Scraping and Calculation tool

Personal project to get a deeper understanding of sports analytics, to leverage for story telling later on for lower-tier leagues. The repository is going to be broken down into the following sections, and their respective programs:

- **Tools:** This folder contains the main scraping and parsing engines used for data gathering (specifically made for fbref.com). The programs gather, aggregate, parse, and output data to JSON files that are used to feed the calculation engine. Currently old parsing files are migrated and combined into one scraping engine running on a Jupyter Notebook - Once completed, a pure python file will be generated for ease of running in a GUI.

  1. *'match_data_parser.ipynb'* is the main Jupyter-based GUI for downloading a full team database, as well as capturing match-level data for a team, on a season-by-season basis. These are produced into JSON files to be consumed by the calculation engine (for now each season's games dumped into one file respectively).

  2. *'match_data_calculator.ipynb'* is the main game instance calculation engine, that will capture match-level data as per generated on the above scraping tool. Currently in a very early interation, and will need refinement when the parser is fully completed.

- **Database_API:** API used to establish DB connections (to MongoDB), and data captures for calculator processing. Currently only runs to test connectivity.

- **Reading:** Contains all the materials that are used for inspiration on the project, as well as some prove-outs of my methods on some simple calculations for illustrative purposes.

  1. *'Prove_Outs'* has example manual calculations for the over-90 metrics, and any other calculation prove-outs that are produced.
  
  2. *'White_Papers'* contains all white papers that are used as inspiration for the calculations, as well as some of which will be also used to produce some prove-outs of the models. This list of course isn't exhaustive, but is both the inspiration behing this, as well as the source of some further thought on the latter half of the build. For now these are rather far from full implementation.
  
- **Old_Files:** This is a dump folder where I have placed all my older variants of the parsing, and calculation engines. These are no longer in use, and are simple retained for posterity. Will likely remove these eventually, however for now I am keeping them in place for my own reference, and in case anyone wants to see the progress of the project from its initial iteration.

### Currently building for the data handler:

**The Scraping Engine:**

- [x] Adjusted for the scraping of the game list for a season.
- [x] Built parser to run through season automatically, instead of game-by-game via manual entry.
- [ ] Built simple statistical inference for 'conceded' statistics.
- [x] Capture main game statistics.
- [ ] Adding some additional metrics to be captured.
- [ ] Add a (SQL) database to handle match data, instead of individual JSON files.

### Scraping Engine Optimizations:

- [ ] Add timing captures for process logging - needed for proper troubleshooting in optimization.

### Currently building for the calculation engine:

- [ ] Fundamental re-write still underway - calculation engine is currently bare-bones.
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
- https://www.fbref.com/
- https://www.github.com/jalapic/engsoccerdata
