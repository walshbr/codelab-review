# brings in the csv library
import csv
from statistics import mean

# 1. before you get into python - put your stuff in the same folder
#   STEP 1 - DONE
# 2. point your program to that data
joseph_file_to_work_with = "uscrime.csv"
susan_file_to_work_with = "MANUSCRITOxml.xml"
# STEP 2 - Done
# 3. get the data in
# use the pointer to the file to actually open it, and name that opened thing 'csvfile'
with open(joseph_file_to_work_with, newline='') as csvfile:
    # take that file, read it in, and store it as "crimereader"
    crimereader = csv.DictReader(csvfile)
    # crimereader - has all of our spreadsheet data in it
    # loop over every line in the crimereader csv 
    southern = []
    northern = []
    for line in crimereader:
        # using "So" (southern state) and "U2" (unemployment rate)
        # can we see if the unemployment rate is higher for southern or northern rates?
        # need to get all the southern stuff together and all the northern stuff together
        if line["So"] == '1':
            # if the line is southern take it out and store it
            southern.append(int(line['U2']))
        else:
            # if the line is northern take it out and store it
            northern.append(int(line['U2']))
print(mean(southern))
print('====')
print(mean(northern))

