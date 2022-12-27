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
    with open(filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = separator, quotechar= quote )
        dict_from_csv = dict(list(csvreader)[0])
        return list(dict_from_csv.keys())



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
        csvreader = csv.DictReader(csvfile, delimiter = separator, quotechar= quote )
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
        csvreader = csv.DictReader(csvfile, delimiter = separator, quotechar= quote )
        for row in csvreader:
            table[row[keyfield]] = row
  
    return table

#print(read_csv_as_nested_dict(r"C:\Users\HP\Desktop\sample1.csv","City", ",", '"'))

def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - nTKame of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
    K  Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """

    with open(filename, "w", newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter = separator, quotechar= quote)
        csvwriter.writeheader()
        csvwriter.writerows(table)


#table_writed_file

#write_csv_from_list_dict("statistics.csv", statistics, fields, ",", "'")