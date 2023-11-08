import pandas as pd
import json
import numpy as np

data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/STIM.csv')

data = data.sample(frac=1).reset_index(drop=True)  # shuffle the entire dataframe

split_data = np.array_split(data, 16)  # split the dataframe into 16 groups

output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/randomize_everything.json'  # Specify the full path to the desired directory and filename
    
print("Size, [small, medium, large]")
print("Culture, [US, JP]]")
print("place, [hotel, school, post office]")
print("direct, [a,b,x,y]")

groups = {}
for i, group in enumerate(split_data):
    size = [0,0,0]
    culture = [0,0]
    place = [0,0,0]
    direct = {"a": 0, "b": 0, "x": 0, "y": 0} 
    
    for index, row in group.iterrows():
        size[row['size'] - 1] += 1
        culture[row['culture'] - 1] += 1
        if row['place'] == 'h':
            place[0] += 1
        elif row['place'] == 's':
            place[1] += 1
        else:
            place[2] += 1
        direct[row['direct']] += 1  # Increase count for value in 'direct' column



    print("--------------------")
    print("Group = " + str(i))
    print(f"{size=}, {culture=}, {place=}, {direct=}")
    
    
    groups[f"{i+1}"] = group.to_dict(orient="records")  # group number as key

with open(output_json_path, 'w') as json_file:  # single file outside loop
    json.dump(groups, json_file, indent=4)



    print("Conversion from CSV to JSON completed successfully.")