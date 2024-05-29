import csv
import json

# define the input file, output directory, and json file
output_directory = './output'
json_file = 'MesObservationGlucose.json'
csv_file = 'InputGlycemiaRawData.csv'


# create a function to read the csv file


def read_csv():
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        # skip the first 19 rows
        glycemia_readings = []
        for _ in range(19):
            next(reader)
        # for each row
        for row in reader:
            split_list = row[0].split(';')
            timestamp = split_list[1].strip('"')
            glycemia_value = split_list[7].strip('"')
            # append the two elements to the glycemia_readings list
            glycemia_readings.append((timestamp, glycemia_value))
        return glycemia_readings


# create a data object from the json file


def create_data():
    with open(json_file, 'r') as f:
        data = json.load(f)
        return data


# define list as the list of glycemia readings
list = read_csv()

# define data_canvas as the data object from the json file
data_canvas = create_data()

# iterate through the list to create a json
for i in list:
    # retrieve the timestamp and the glycemia value
    timestamp = i[0]
    glycemia_value = i[1]
    # modify the data_canvas accordingly
    data_canvas['effectiveDateTime'] = timestamp
    data_canvas['valueQuantity']['value'] = glycemia_value
    # create a new json file in the output directory with the data_canvas
    # using the timestamp as the name of the file
    with open(f'{output_directory}/{timestamp}.json', 'w') as f:
        json.dump(data_canvas, f)

# end of mapping.py
