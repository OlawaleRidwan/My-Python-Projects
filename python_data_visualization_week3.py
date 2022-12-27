import csv
import math

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


def reconcile_countries_by_name(plot_countries, gdp_countries):
    present_countries_dict = {}
    not_present_countries_set = set()

    for country_name in gdp_countries:
        for country_code in plot_countries:
            if plot_countries[country_code] == country_name:
                present_countries_dict[country_code] = plot_countries[country_code]

    for country_code in plot_countries:
        if present_countries_dict.get(country_code) is None:
            not_present_countries_set.add(country_code)

    return present_countries_dict, not_present_countries_set


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    gdp_countries = read_csv_as_nested_dict(
        gdpinfo["gdpfile"], gdpinfo["country_name"], gdpinfo["separator"], gdpinfo["quote"])

    reconciled_names = reconcile_countries_by_name(
        plot_countries, gdp_countries)

    present_countries_dict = reconciled_names[0]
    not_present_country_codes_set = reconciled_names[1]

    present_empty_data_countries_code = set()
    present_countries_data_dict = {}

    for code, name in present_countries_dict.items():
        gdp_in_year = gdp_countries[name].get(year)
        if gdp_in_year in ('0', ""):
            present_empty_data_countries_code.add(code)
        else:
            present_countries_data_dict[code] = math.log(float(gdp_in_year), 10)

    return present_countries_data_dict, not_present_country_codes_set, present_empty_data_countries_code



















