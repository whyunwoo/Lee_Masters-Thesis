import pandas as pd
import json
import numpy as np

# Load CSV file
data = pd.read_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-Lee_Thesis/assets/img/stimuli_grouping/stimgrouping.csv')

# Add place and size as random
location_type = ["sch", "pos"]
sizes = ["small", "middle", "large"]

data["location_type"] = np.random.choice(location_type, len(data))
data["size"] = np.random.choice(sizes, len(data))

print("Culture, [wheat, rice]")

output_log_columns = ['Group', 'Culture_Count', 'Size_Count', 'Location_Type_Count', 'Total_Pictures']
output_log = pd.DataFrame(columns=output_log_columns)

groups = {}
total_pictures_per_group = 48
group_count = 8

while len(data) >= total_pictures_per_group and len(groups)<group_count:
    sample_size_WHEAT = min(len(data[data['culture'] == 1]), total_pictures_per_group // 2)
    sample_size_RICE = min(len(data[data['culture'] == 2]), total_pictures_per_group // 2)

    # Here we make sure that we have enough data left for the other groups
    if len(data) - sample_size_WHEAT - sample_size_RICE < (group_count - len(groups) - 1) * total_pictures_per_group:
        break

    df_WHEAT = data[data['culture'] == 1].sample(sample_size_WHEAT, replace=False)
    df_RICE = data[data['culture'] == 2].sample(sample_size_RICE, replace=False)

    data = data.drop(df_WHEAT.index)
    data = data.drop(df_RICE.index)

    group = pd.concat([df_WHEAT, df_RICE])

    size_count = group['size'].value_counts().to_dict()
    culture_count = group['culture'].value_counts().to_dict()
    location_type_count = group['location_type'].value_counts().to_dict()

    culture_count_str = f"(1: {culture_count.get(1, 0)}, 2: {culture_count.get(2, 0)})"
    size_count_str = f"(large: {size_count.get('large', 0)}, middle: {size_count.get('middle', 0)}, small: {size_count.get('small', 0)})"
    location_type_count_str = f"(sch: {location_type_count.get('sch', 0)}, pos: {location_type_count.get('pos', 0)})"

    log_item = pd.DataFrame([{
        'Group': len(groups) + 1,
        'Culture_Count': culture_count_str,
        'Size_Count': size_count_str,
        'Location_Type_Count': location_type_count_str,
        'Total_Pictures': len(group)
    }])

    output_log = pd.concat([output_log, log_item], ignore_index=True)
    groups[len(groups) + 1] = group[['name', 'size', 'culture', 'location_type', 'number']].to_dict('records')

# Save output log to a CSV file
output_log.to_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-Lee_Thesis/assets/scripts/output_log.csv', index=False)

# Save leftover data to a CSV file
leftover_data = pd.concat([data])
leftover_data.to_csv('/Users/arajo/Documents/01. Project/perceptual-affordance-Lee_Thesis/assets/scripts/leftover_data.csv', index=False, sep='\t')

# Save grouped JSON file
output_json_path = '/Users/arajo/Documents/01. Project/perceptual-affordance-Lee_Thesis/assets/scripts/groups.json'
with open(output_json_path, 'w') as json_file:
    json.dump(groups, json_file, indent=4)


print("Conversion from CSV to JSON completed successfully.")