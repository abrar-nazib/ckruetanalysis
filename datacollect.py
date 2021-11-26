import fitz
file1 = fitz.open("buet.pdf")

# extracting text elements from buet.pdf file and saving it into buet.txt
for pageNumber, page in enumerate(file1.pages(), start=1):
    text = page.get_text()
    txt = open(f'buet.txt', 'a')
    txt.writelines(text)
    txt.close()

file2 = fitz.open("kuet.pdf")
# extracting text elements from kuet.pdf file and saving it into ckruet.txt
for pageNumber, page in enumerate(file2.pages(), start=1):
    text = page.get_text()
    txt = open(f'ckruet.txt', 'a')
    txt.writelines(text)
    txt.close()

file3 = fitz.open("ruet.pdf")
# extracting text elements from ruet.pdf file and appending it into ckruet.txt
for pageNumber, page in enumerate(file3.pages(), start=1):
    text = page.get_text()
    txt = open(f'ckruet.txt', 'a')
    txt.writelines(text)
    txt.close()

file4 = fitz.open("cuet.pdf")

# extracting text elements from cuet.pdf file and saving it into ckruet.txt
for pageNumber, page in enumerate(file4.pages(), start=1):
    text = page.get_text()
    txt = open(f'ckruet.txt', 'a')
    txt.writelines(text)
    txt.close()
