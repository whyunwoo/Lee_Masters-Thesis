import csv
import json

# Provide the correct path to your CSV file
csv_file_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/stim/g.all.csv'

try:
    with open(csv_file_path, 'r', newline='') as csv_file:  # Add newline='' for cross-platform compatibility
        csv_reader = csv.DictReader(csv_file, delimiter=',')  # Specify tab ('\t') as the delimiter

        data = []

        for row in csv_reader:
            entry = {
                "group": row['\ufeffgroup'],
                "picture": row['picture'],
                "Condition": row['Condition'],
                "size": row['size'],
                "culture": row['culture'],
                "place": row['place'],
                "direct": row['direct'],
                "street": row['street'],
                "back": row['back']
            }
            data.append(entry)

    output_json = json.dumps(data, indent=2)

    with open('test.json', 'w') as json_file:
        json_file.write(output_json)

    print("Conversion from CSV to JSON completed successfully.")

except Exception as e:
    print("An error occurred:", str(e))
