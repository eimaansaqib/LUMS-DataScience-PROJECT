import json
import csv

file_name = 'xboxone'

with open('JSON Files\\'+file_name + '.json') as f:
    dataset = json.load(f)

# dataset = [json.loads(line) for line in open('ps4.json', 'r')]

csv_file = open('CSV Files\\' + file_name + '.csv', 'w', newline='')
csv_write = csv.writer(csv_file)

columns =  list({column for row in dataset for column in row.keys()})
csv_write.writerow(columns)

for row in dataset:
    csv_write.writerow([None if column not in row else row[column] for column in columns])

# counter = 0
# for data in dataset:
#     if counter == 0:
#         header = data.keys()
#         csv_write.writerow(header)
#         counter += 1
#     csv_write.writerow(data.values())

csv_file.close()