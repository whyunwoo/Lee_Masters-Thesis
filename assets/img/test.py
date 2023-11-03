import csv
import json

# Provide the correct path to your CSV file
csv_file_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/g.all.csv'

try:
    with open(csv_file_path, 'r', newline='') as csv_file:  # Add newline='' for cross-platform compatibility
        csv_reader = csv.DictReader(csv_file, delimiter=',')  # Specify comma (',') as the delimiter

        groups = {}

        for row in csv_reader:
            group_key = row['\ufeffgroup']
            entry = {
                "name": row['picture'],
                "Condition": row['Condition'],
                "size": row['size'],
                "culture": row['culture'],
                "place": row['place'],
                "direct": row['direct'],
                "street": row['street'],
                "back": row['back']
            }
            if group_key in groups:
                groups[group_key][row['picture']] = entry
            else:
                groups[group_key] = {row['picture']: entry}

    output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/test.json'  # Specify the full path to the desired directory and filename
    output_json = json.dumps(groups, indent=2)

    with open(output_json_path, 'w') as json_file:
        json_file.write(output_json)

    print("Conversion from CSV to JSON completed successfully.")

except Exception as e:
    print("An error occurred:", str(e))
