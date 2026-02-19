import csv
input_list=[
    ['Thomas',22,'CSE','England'],
    ['Georgia',25,'CSE','America'],
    ['Sam',26,'ME','England']
]
with open('output.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerows(input_list)