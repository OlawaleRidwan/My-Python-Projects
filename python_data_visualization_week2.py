
import csv
import pygal


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(
            csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table



def build_plot_values(gdpinfo, gdpdata):
    values_for_plot = []
    min_year = gdpinfo["min_year"]
    max_year = gdpinfo["max_year"]

    for each_year in range(min_year, max_year + 1):
        gdp = gdpdata.get(str(each_year))
        if gdp == "" or gdp is None:
            continue
        values_for_plot.append((each_year, float(gdp)))

    return values_for_plot



def build_plot_dict(gdpinfo, country_list):
    gdp_data_values = read_csv_as_nested_dict(
        gdpinfo["gdpfile"], gdpinfo["country_name"], gdpinfo["separator"], gdpinfo["quote"])

    plot_values_dict = dict()
    for each_country in country_list:
        each_country_data = gdp_data_values.get(each_country)
        if each_country_data is None:
            plot_values_dict[each_country] = []
        else:
            plot_values_dict[each_country] = build_plot_values(gdpinfo, each_country_data)

    return plot_values_dict



def render_xy_plot(gdpinfo, country_list, plot_file):
    coords = build_plot_dict(gdpinfo, country_list)

    graph_plot = pygal.XY(height=400)
    graph_plot.title = " - ".join(country_list).upper() + " GDP Line Graph"
   
    for country_names in country_list:
        graph_plot.add(country_names, coords[country_names])
    graph_plot.render_to_file(plot_file)
    






