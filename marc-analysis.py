from os import read
import bs4

susan_file_to_work_with = "MANUSCRITOxml.xml"

with open(susan_file_to_work_with, 'r') as file_in:
    read_file = file_in.read()

soup = bs4.BeautifulSoup(read_file, 'html.parser')
print(soup)