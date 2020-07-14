
import csv

# field names
fields = ['Name', ' fullpath,   ', 'Data created ', 'last modified','file extension']

# data rows of csv file
rows = [ [ ['
# name of csv file
filename = "new.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)