"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

##
## Provided code from Week 3 Project
##

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table

table_readed_file = read_csv_as_list_dict(r"C:\Users\HP\Desktop\sample1.csv", ",", '"')

print(table_readed_file)


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0




baseballdatainfo = {
        "masterfile": "Master_2016.csv",   # Name of Master CSV file
        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
        "separator": ",",                  # Separator character in CSV files
        "quote": '"',                      # Quote character in CSV files
        "playerid": "playerID",            # Player ID field name
        "firstname": "nameFirst",          # First name field name
        "lastname": "nameLast",            # Last name field name
        "yearid": "yearID",                # Year field name
        "atbats": "AB",                    # At bats field name
        "hits": "H",                       # Hits field name
        "doubles": "2B",                   # Doubles field name
        "triples": "3B",                   # Triples field name
        "homeruns": "HR",                  # Home runs field name
        "walks": "BB",                     # Walks field name
        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]
    }

##
## Part 1: Functions to compute top batting statistics by year
##




def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    
    new_statistics = list(filter(lambda stat: int(stat[yearid]) == year   , statistics))
    return new_statistics

#print("")
#print(filter_by_year(table_writed_file,62, "Jan"))


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and 
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """

    player_id_list = list(map(lambda stats:stats[info['playerid']]  ), statistics)
    comp_stat_list = list(map(lambda stats: formula(info, stats), statistics))
    
    #create list of tuples
    tups = list(map(lambda player_id,comp_stat: (player_id,comp_stat), player_id_list, comp_stat_list))

    # sort the above list by the second element in each tuple in descending order
    tups.sort(key = lambda pair: pair[1], reverse=True)

    #sorted lists in descending order of the of number of top players
    final_tups = tups[:numplayers]


top_player_ids({'masterfile': '', 'battingfile': '', 'separator': ',', 'quote': '"', 
'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year', 
'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks', 
'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']}, [{'hits': '108', 'year': '2020', 'homers': '5', 'player': 'player0', 'atbats': '300', 'doubles': '20', 'walks': '25', 'triples': '1'},
{'hits': '170', 'year': '2020', 'homers': '4', 'player': 'player1', 'atbats': '499', 'doubles': '5', 'walks': '10', 'triples': '3'},
{'hits': '129', 'year': '2020', 'homers': '20', 'player': 'player2', 'atbats': '513', 'doubles': '18', 'walks': '85', 'triples': '5'},
{'hits': '67', 'year': '2020', 'homers': '22', 'player': 'player5', 'atbats': '197', 'doubles': '3', 'walks': '37', 'triples': '2'},
{'hits': '166', 'year': '2020', 'homers': '18', 'player': 'player6', 'atbats': '542', 'doubles': '33', 'walks': '25', 'triples': '7'},
{'hits': '161', 'year': '2020', 'homers': '10', 'player': 'player7', 'atbats': '500', 'doubles': '19', 'walks': '27', 'triples': '2'},
{'hits': '176', 'year': '2020', 'homers': '25', 'player': 'player8', 'atbats': '589', 'doubles': '42', 'walks': '30', 'triples': '13'}], batting_average({'masterfile': '', 'battingfile': '', 'separator': ',', 'quote': '"', 
'playerid': 'player', 'firstname': 'firstname', 'lastname': 'lastname', 'yearid': 'year', 
'atbats': 'atbats', 'hits': 'hits', 'doubles': 'doubles', 'triples': 'triples', 'homeruns': 'homers', 'walks': 'walks', 
'battingfields': ['atbats', 'hits', 'doubles', 'triples', 'homers', 'walks']}, [{'hits': '108', 'year': '2020', 'homers': '5', 'player': 'player0', 'atbats': '300', 'doubles': '20', 'walks': '25', 'triples': '1'},
{'hits': '170', 'year': '2020', 'homers': '4', 'player': 'player1', 'atbats': '499', 'doubles': '5', 'walks': '10', 'triples': '3'},
{'hits': '129', 'year': '2020', 'homers': '20', 'player': 'player2', 'atbats': '513', 'doubles': '18', 'walks': '85', 'triples': '5'},
{'hits': '67', 'year': '2020', 'homers': '22', 'player': 'player5', 'atbats': '197', 'doubles': '3', 'walks': '37', 'triples': '2'},
{'hits': '166', 'year': '2020', 'homers': '18', 'player': 'player6', 'atbats': '542', 'doubles': '33', 'walks': '25', 'triples': '7'},
{'hits': '161', 'year': '2020', 'homers': '10', 'player': 'player7', 'atbats': '500', 'doubles': '19', 'walks': '27', 'triples': '2'},
{'hits': '176', 'year': '2020', 'homers': '25', 'player': 'player8', 'atbats': '589', 'doubles': '42', 'walks': '30', 'triples': '13'}]), 4)


def lookup_player_names(info, top_ids_and_stats):
 
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    return []


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    return []


##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    return {}


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    return []


##
## Provided testing code
##

def test_baseball_statistics():
    """
    Simple testing code.
    """
 #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

# test_baseball_statistics()