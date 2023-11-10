import pandas as pd
import json

data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/STIM.csv')

group1 = data[(data['culture'] == 1) & (data['direct'].isin(['a', 'b']))].sample(frac=1).reset_index(drop=True)
group2 = data[(data['culture'] == 2) & (data['direct'].isin(['a', 'b']))].sample(frac=1).reset_index(drop=True)
group3 = data[(data['culture'] == 1) & (data['direct'].isin(['x', 'y']))].sample(frac=1).reset_index(drop=True)
group4 = data[(data['culture'] == 2) & (data['direct'].isin(['x', 'y']))].sample(frac=1).reset_index(drop=True)

groupab = pd.concat([group1, group2]).sample(frac=1).reset_index(drop=True)
groupxy = pd.concat([group3, group4]).sample(frac=1).reset_index(drop=True)

chunks = [groupab, groupxy]

output_data = []
for i, chunk in enumerate(chunks):
    n = len(chunk) // 8  # Size of each group
    chunk_groups = [chunk[j:j + n] for j in range(0, len(chunk), n)] 
    output_data += chunk_groups[:8]  # Take the first 8 groups from each chunk

groups = {}
output_log = []

for i, group in enumerate(output_data):
    size = [0, 0, 0]
    culture = [0, 0]
    place = [0, 0, 0]
    direct = {"a": 0, "b": 0, "x": 0, "y": 0}

    for _, row in group.iterrows():
        size[row['size'] - 1] += 1
        culture[row['culture'] - 1] += 1
        if row['place'] == 'h':
            place[0] += 1
        elif row['place'] == 's':
            place[1] += 1
        else:
            place[2] += 1
        direct[row['direct']] += 1

    output_log.append("--------------------")
    output_log.append(f"Group = {i+1}")
    output_log.append(f"{size=}, {culture=}, {place=}, {direct=}")
    output_log.append("Number of pictures in the group: " + str(len(group)))  # Print total number of pictures in the group

    groups[f"{i+1}"] = group.to_dict(orient="records")

# Save the print statements to a text file
output_txt_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/output_log.txt'
with open(output_txt_path, 'w') as txt_file:
    txt_file.write('\n'.join(output_log))

# Save the results to a JSON file
output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/randomize_equally.json'
with open(output_json_path, 'w') as json_file:
    json.dump(groups, json_file, indent=4)

print("Conversion from CSV to JSON completed successfully.")
