#!/usr/bin/python3
import fitz
import re
import csv

file1 = fitz.open("ka18.pdf")
csv_file = open('MTE.csv', "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Roll', 'Name', 'Merit', 'Subject'])
# extracting text elements from buet.pdf file and saving it into buet.txt
for pageNumber, page in enumerate(file1.pages(), start=1):
    text = page.get_text()
    txt = open(f'store.txt', 'a')
    txt.writelines(text)
    txt.close()

data_dict = []
with open('store.txt') as storefile:
    storefile_content = storefile.read()
    pattern = re.compile('(\d{5})\n(\w+)\n(.+)\n(\d+)\n(.+)')
    matches = pattern.finditer(storefile_content)
    for match in matches:
        data_elem = {}
        data_elem["Roll"] = match.group(1)
        data_elem["Name"] = match.group(3)
        data_elem["Merit"] = match.group(4)
        data_elem["Subject"] = match.group(5)
        data_dict.append(data_elem)

for student in data_dict:
    if(student["Subject"] == "MTE-RUET"):
        csv_writer.writerow(
            [student['Roll'], student['Name'], student['Merit'], student['Subject']])
csv_file.close()
