import pandas as pd
import json
import numpy as np

data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/img/stimuli_grouping/STIM.csv')

# Add place and size as random
places = ["hotel", "school", "post office"]
sizes = ["small", "middle", "large"]

data["place"] = np.random.choice(places, len(data))
data["size"] = np.random.choice(sizes, len(data))

print("Culture, [US, JP]")
print("Direction, [a,b,x,y]")

groups = {}

output_log = pd.DataFrame(columns=['Group', 'Culture_Count', 'Size_Count', 'Place_Count', 'Direct_Count', 'Total_Pictures'])

data_US = data[(data['culture']==1) & ((data['direct'] == 'a') | (data['direct'] == 'b'))]
data_JP = data[(data['culture']==2) & ((data['direct'] == 'a') | (data['direct'] == 'b'))]
data_US_XY = data[(data['culture']==1) & ((data['direct'] == 'x') | (data['direct'] == 'y'))]
data_JP_XY = data[(data['culture']==2) & ((data['direct'] == 'x') | (data['direct'] == 'y'))]

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

    culture_count_str = f"(1: {culture_count.get(1, 0)}, 2: {culture_count.get(2, 0)})"
    size_count_str = f"(large: {size_count.get('large', 0)}, middle: {size_count.get('middle', 0)}, small: {size_count.get('small', 0)})"
    place_count_str = f"(school: {place_count.get('school', 0)}, postoffice: {place_count.get('post office', 0)}, hotel: {place_count.get('hotel', 0)})"
    direction_count_str = f"(a: {direct_count.get('a', 0)}, b: {direct_count.get('b', 0)}, x: {direct_count.get('x', 0)}, y: {direct_count.get('y', 0)})"

    log_item = pd.DataFrame([{
        'Group': f"{i+1}",
        'Culture_Count': culture_count_str,
        'Size_Count': size_count_str,
        'Place_Count': place_count_str,
        'Direct_Count': direction_count_str,
        'Total_Pictures': len(group)
    }])

    output_log = pd.concat([output_log, log_item], ignore_index=True)
    groups[f"{i+1}"] = group.to_dict(orient="records")

# Save output
output_log.to_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/scripts/output_log.csv', index=False)

# Save leftover data to a CSV file
leftover_data = pd.concat([data_US, data_JP, data_US_XY, data_JP_XY])
leftover_data.to_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/scripts/leftover_data.csv', index=False, sep='\t')

# Save grouped json file
output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-OriginalStimuli/assets/scripts/groups.json'
with open(output_json_path, 'w') as json_file:
    json.dump(groups, json_file, indent=4)

print("Conversion from CSV to JSON completed successfully.")