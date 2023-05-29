from bs4 import BeautifulSoup
import requests
import xlsxwriter


def parse():
    url = 'https://auto.drom.ru/'
    page = requests.get(url)
    print(page.status_code)
    for key, value in page.request.headers.items():
        print(key + ": " + value)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', class_='css-l1wt7n e3f4v4l2')
    block_price = soup.findAll('div', class_='css-1dv8s3l eyvqki91')
    description = []
    descriptionPrice = []

    for data in block:
        if data.find('span'):
            description.append(data.text)

    for data in block_price:
        if data.find('span'):
            descriptionPrice.append(data.text)

    book = xlsxwriter.Workbook('home.xlsx')
    sheet = book.add_worksheet()
    print(description)

    row = 0
    column = 0

    for item in description:
        sheet.write(row, column, item)
        row += 1
    row = 0
    for item in descriptionPrice:
        sheet.write(row, column + 1, item)
        row += 1
    book.close()


parse()
