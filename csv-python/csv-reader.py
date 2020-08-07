import csv

file_source = open('sales.csv')
file_reader = csv.reader(file_source)

file_list = list(file_reader)

# print_file = print(file_list[0]) #print the list

print(len(file_list))

region = []
country = []
item_type = []
sales_channel = []
order_priority = []
order_date = []
order_id = []


for countries in file_list:
  country.append(countries[1])

print(country)