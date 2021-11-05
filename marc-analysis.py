from bs4 import BeautifulSoup

# store the filepath
susan_file_to_work_with = "MANUSCRITOxml.xml"

# open that file and just pull it all in as a string
with open(susan_file_to_work_with, 'r') as file_in:
    read_file = file_in.read()

# turn that string into soup
soup = BeautifulSoup(read_file, 'html.parser')

# find the records using the marc:record tag
records = soup.find_all('marc:record')
for record in records:
    # go through each record and print out a particular tag combination. physical dimensions in this case
    if record.find('marc:datafield', tag="336"):
        print(record.find('marc:datafield', tag="336").text)

records = soup.find_all('marc:subfield', code="z")
for record in records:
    print(record.text)