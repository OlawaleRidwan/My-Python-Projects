import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, skipinitialspace=True, delimiter = separator, quotechar= quote )
        return csvreader.fieldnames


fields = read_csv_fieldnames(r"C:\Users\HP\Desktop\sample1.csv", ",", '"')


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


    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, skipinitialspace=True, delimiter = separator, quotechar= quote )
        for row in csvreader:
            table.append(row)
    
    return table

#table_readed_file =(read_csv_as_list_dict(r"C:\Users\HP\Desktop\sample1.csv", ",", '"'))
#print(read_csv_as_list_dict(r"C:\Users\HP\Desktop\sample1.csv", ",", '"'))

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


    with open(filename, "rt", newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, skipinitialspace=True, delimiter = separator, quotechar= quote )
        for row in csvreader:
            table[row[keyfield]] = row
    
    return table

statistics = [{'hits': '108', 'year': '2020', 'homers': '5', 'player': 'player0', 'atbats': '300', 'doubles': '20', 'walks': '25', 'triples': '1'},
{'hits': '170', 'year': '2020', 'homers': '4', 'player': 'player1', 'atbats': '499', 'doubles': '5', 'walks': '10', 'triples': '3'},
{'hits': '129', 'year': '2020', 'homers': '20', 'player': 'player2', 'atbats': '513', 'doubles': '18', 'walks': '85', 'triples': '5'},
{'hits': '67', 'year': '2020', 'homers': '22', 'player': 'player5', 'atbats': '197', 'doubles': '3', 'walks': '37', 'triples': '2'},
{'hits': '166', 'year': '2020', 'homers': '18', 'player': 'player6', 'atbats': '542', 'doubles': '33', 'walks': '25', 'triples': '7'},
{'hits': '161', 'year': '2020', 'homers': '10', 'player': 'player7', 'atbats': '500', 'doubles': '19', 'walks': '27', 'triples': '2'},
{'hits': '176', 'year': '2020', 'homers': '25', 'player': 'player8', 'atbats': '589', 'doubles': '42', 'walks': '30', 'triples': '13'}]

#print(read_csv_as_nested_dict(r"C:\Users\HP\Desktop\sample1.csv","City", ",", '"'))

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """

    with open(filename, "w", newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = separator, quotechar= quote)
        csvwriter.writeheader()
        csvwriter.writerows(table)


#table_writed_file

write_csv_from_list_dict("statistics.csv", statistics, fields, ",", "'")