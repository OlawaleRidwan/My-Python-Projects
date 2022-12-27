"""
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

import csv
import math


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    table = {}
    with open(filename, "rt", newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


def build_country_code_converter(codeinfo):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    country_codes_data = read_csv_as_nested_dict(
        codeinfo["codefile"], codeinfo["plot_codes"], codeinfo["separator"], codeinfo["quote"])

    plot_to_gdp_codes = {}
    for each_data in country_codes_data.values():
        plot_codes = each_data[codeinfo["plot_codes"]]
        gdp_codes = each_data[codeinfo["data_codes"]]
        plot_to_gdp_codes[plot_codes] = gdp_codes
    return plot_to_gdp_codes


def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    plot_to_wb_codes = build_country_code_converter(codeinfo)
    present_countries_dict = {}
    not_present_countries_set = set()

    for each_gdp_code in gdp_countries:
        for each_plot_code in plot_countries:
            if plot_to_wb_codes[each_plot_code.upper()] == each_gdp_code:
                present_countries_dict[each_plot_code] = plot_to_wb_codes[each_plot_code.upper(
                )]

    for each_plot_code in plot_countries:
        if present_countries_dict.get(each_plot_code) is None:
            not_present_countries_set.add(each_plot_code)

    return present_countries_dict, not_present_countries_set



def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.
      
      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    gdp_countries = read_csv_as_nested_dict(
        gdpinfo["gdpfile"], gdpinfo["country_code"], gdpinfo["separator"], gdpinfo["quote"])

    reconciled_names = reconcile_countries_by_code(codeinfo,
        plot_countries, gdp_countries)

    present_countries_dict = reconciled_names[0]
    not_present_country_codes_set = reconciled_names[1]

    found_empty_data_countries_code = set()
    found_countries_data_dict = {}
    
    for each_plot_code, each_gdp_code in present_countries_dict.items():
        gdp_in_year = gdp_countries[each_gdp_code].get(year)
        if gdp_in_year in ('0', ""):
            found_empty_data_countries_code.add(each_plot_code)
        else:
            found_countries_data_dict[each_plot_code] = math.log(float(gdp_in_year), 10)

    return found_countries_data_dict, not_present_country_codes_set, found_empty_data_countries_code

