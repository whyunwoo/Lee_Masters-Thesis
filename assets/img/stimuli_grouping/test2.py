import pandas as pd
import json
import numpy as np

data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/img/STIM.csv')

names = list(data['name'])

print(names)


np.random.shuffle(names)

shuffle_names = np.array_split(list(names), 16)

shuffle_names = [list(names) for names in shuffle_names]

output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-orig.stim/assets/scripts/test1.json'  # Specify the full path to the desired directory and filename

output_json = json.dumps(shuffle_names, indent=2)

with open(output_json_path, 'w') as json_file:
    json_file.write(output_json)
    
print("Size, [small, medium, large]")
print("Culture, [US, JP]]")
print("place, [hotel, school, post office]")

    
for i in range(16):
    
    size = [0,0,0]
    culture = [0,0]
    place = [0,0,0]
    
    for name in shuffle_names[i]:
        
        idx = data.name[data.name == name].index[0]
        
        row = data.iloc[idx]
        size[row['size'] - 1] += 1
        culture[row['culture'] - 1] += 1
        if row['place'] == 'h':
            place[0] += 1
        elif row['place'] == 's':
            place[1] += 1
        else:
            place[2] += 1

    print("--------------------")
    print("Group = " + str(i))
    print(f"{size=}, {culture=}, {place=}")
    
    
    with open(output_json_path, 'w') as json_file:
        json_file.write(output_json)

    print("Conversion from CSV to JSON completed successfully.")