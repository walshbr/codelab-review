from bs4 import BeautifulSoup

susan_file_to_work_with = "MANUSCRITOxml.xml"

with open(susan_file_to_work_with, 'r') as file_in:
    read_file = file_in.read()

soup = BeautifulSoup(read_file, 'html.parser')
records = soup.find_all('marc:record')
for record in records:
    if record.find('marc:datafield', tag="300"):
        print(record.find('marc:datafield', tag="300").text)
    # for child in record.children:
    #     print(child)
    #     print(child.name)