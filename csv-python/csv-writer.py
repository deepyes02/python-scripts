import csv
output_file = open('output.csv', 'w', newline="")
output_writer = csv.writer(output_file)
output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])

output_writer.writerow(['Hello World', 'eggs', 'bacon', 'ham'])

output_writer.writerow(['1','2','3.134','4','5'])

output_file.close()