# Football Scraping and Calculation tool

Personal project to get a deeper understanding of sports analytics, to leverage for story telling later on for lower-tier leagues. The repository is going to be broken down into the following sections, and their respective programs:

- Calculators: Contains the calculators used to do analysis on the scraped data files. Currently consists only of 'season_calcs.py'. 'season_calcs.py' is a program that at this time simply recaps the team season-by-season data, and creates a summary of it fronm 2002-present. This includes all main captured data, as well as calculated over-90 calculations.
- Data_Files: Has some example data files within it for calculation testing (these have been scraped, and produced as-is), as well as an example data urls file for list-based scraping. The latter is still in testing, as it hasn't worked too reliably.
- Prove_Outs: Is just a folder for some example manual calculations for the over-90 metrics. This was done in Excel, with one of the season files in Data_Files.
- Scraping_Tools: Is the main engine for the operation, currently able to scrape both team season data (i.e. the data recap for the entire season of a specific team), which is done with the 'team_scraper.py' program. The 'league_scraper.py' on the other hand is designed to capture a full season recap for the league, e.g. the points, goals, differentials for all teams. The latter is also used to produce the league team breakdowns, which will be consolidated to a summary file later for season-by-season team list use. The latter implementation is tentative as of now.
- Test_Files: Is a folder for some of the test.py files that I use as placeholders, while testing specific behavior added to the scraping tools or calculators. None of these are active production files however, and often can be empty if I'm not in the middle of a specific code test.
- White_Papers: Contains all white papers that are used as inspiration for the calculations, as well as some of which will be also used to produce some prove-outs of the models. This list of course isn't exhaustive, but is both the inspiration behing this, as well as the source of some further thought on the latter half of the build. For now these are rather far from full implementation.

# Currently building for the data parser:

- Use Data URLs.xlsx to feed the parser instead of single, manual URLs, for easy team one-off parsing. Current scope simply 2002 onward.
- Use League Two/League One Teams per Season files to feed team listings for parser, to get all teams at once. All needed is the URL team codes, and the rest can be automated.

- Run simply calculations for team performative stats (G/90, A/90, G+A/90, G-PK/90, G+A-PK/90, SOT/90, F/90, C/90) off of parser. Should just be captured rather easily off of the acquired data.

# Currently building for the calculation engine:

- Calculate player performance throughout seasons.
- Replicate FiveThirtyEight model for team success predictions.
- Apply some basic models (TBD) for team level analytics.

# Legend and Notes:

- Calculation notation: Goals (G), Assists (A), Penalties (PK), Shots on Target (SOT), Fouls (F), Cards (C), Per 90 Minutes (/90), Total Minutes Played (TM).
- Math for over 90s is simple, for example G+A-PK/90: (G+A)/(TM/90). The float result effectively will define a simple performance metric to start with. Attached is also a manual prove-out of some of the metrics, as fref has them (Per90 Manual Prove Out.xlsx).
