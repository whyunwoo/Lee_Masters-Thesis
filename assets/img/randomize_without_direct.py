import pandas as pd
import json
import numpy as np


data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/STIM.csv')

# Create separate dataframes based on 'direct' values
data_ab = data[(data['direct'] == 'a') | (data['direct'] == 'b')]
data_xy = data[(data['direct'] == 'x') | (data['direct'] == 'y')]

# Shuffle the dataframes
data_ab = data_ab.sample(frac=1).reset_index(drop=True)
data_xy = data_xy.sample(frac=1).reset_index(drop=True)

# Split the dataframes into 8 groups each
split_data_ab = np.array_split(data_ab, 8)
split_data_xy = np.array_split(data_xy, 8)

# Combine the split data: first 8 groups with 'a' & 'b', last 8 with 'x' & 'y'
split_data = split_data_ab + split_data_xy

output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/randomize_without_direct.json'  # Specify the path

print("Size, [small, medium, large]")
print("Culture, [US, JP]]")
print("Place, [hotel, school, post office]")
print("Direct, [a,b,x,y]")

groups = {}
for i, group in enumerate(split_data):
    size = [0,0,0]
    culture = [0,0]
    place = [0,0,0]
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

    print("--------------------")
    print("Group = " + str(i+1))
    print(f"{size=}, {culture=}, {place=}, {direct=}")
    
    groups[f"{i+1}"] = group.to_dict(orient="records")  # group number as key

with open(output_json_path, 'w') as json_file:  # single file outside loop
    json.dump(groups, json_file, indent=4)

print("Conversion from CSV to JSON completed successfully.")