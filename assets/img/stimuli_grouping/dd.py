import pandas as pd
import json
import numpy as np

data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/img/stimuli_grouping/STIM.csv')

# Add place and size as random
places = ["hotel", "school", "post office"]
sizes = ["small", "medium", "large"]

data["place"] = np.random.choice(places, len(data))
data["size"] = np.random.choice(sizes, len(data))

print("Culture, [US, JP]")
print("Direction, [a,b,x,y]")

groups = {}
output_log = []
data_US = data[(data['culture']==1) & ((data['direct'] == 'a') | (data['direct'] == 'b'))]  # AB direction US images
data_JP = data[(data['culture']==2) & ((data['direct'] == 'a') | (data['direct'] == 'b'))]  # AB direction JP images
data_US_XY = data[(data['culture']==1) & ((data['direct'] == 'x') | (data['direct'] == 'y'))]  # XY direction US images
data_JP_XY = data[(data['culture']==2) & ((data['direct'] == 'x') | (data['direct'] == 'y'))]  # XY direction JP images

for i in range(16):
    if i < 8:
        sample_size_US = min(len(data_US), 30)
        sample_size_JP = min(len(data_JP), 31)
        df_US = data_US.sample(sample_size_US)
        df_JP = data_JP.sample(sample_size_JP)
        data_US = data_US.drop(df_US.index)
        data_JP = data_JP.drop(df_JP.index)
    else:
        sample_size_US = min(len(data_US_XY), 30)
        sample_size_JP = min(len(data_JP_XY), 31)
        df_US = data_US_XY.sample(sample_size_US)
        df_JP = data_JP_XY.sample(sample_size_JP)
        data_US_XY = data_US_XY.drop(df_US.index)
        data_JP_XY = data_JP_XY.drop(df_JP.index)
        
    group = pd.concat([df_US, df_JP])
    
    size_count = group['size'].value_counts().to_dict()
    culture_count = group['culture'].value_counts().to_dict()
    place_count = group['place'].value_counts().to_dict()
    direct_count = group['direct'].value_counts().to_dict()
    
    # Ensure all 4 directions are present in direct_count
    all_directions = ['a', 'b', 'x', 'y']
    for direction in all_directions:
        if direction not in direct_count:
            direct_count[direction] = 0

    output_log.append("--------------------")
    output_log.append(f"{i+1}")
    output_log.append(f"{culture_count=}, {size_count=}, {place_count=}, {direct_count=}")
    output_log.append(f"Number of pictures in the group: {len(group)}")

    groups[f"{i+1}"] = group.to_dict(orient="records")

# Save the print statements to a text file
output_txt_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/scripts/output_log44.txt'
with open(output_txt_path, 'w') as txt_file:
    txt_file.write('\n'.join(output_log))

# Save the results to a JSON file
output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/scripts/dd44.json'
with open(output_json_path, 'w') as json_file:
    json.dump(groups, json_file, indent=4)

print("Conversion from CSV to JSON completed successfully.")


