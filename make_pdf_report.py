from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import csv


def make_pdf_report():
    pdf = SimpleDocTemplate("report.pdf")
    flow_obj = []

    with open("stock.csv", "r") as f:
        stock_report = csv.reader(f)
        tdata = []
        for line in stock_report:
            data = []
            id = line[0]
            date = line[1]
            product = line[2]
            buy_price = line[3]
            amount = line[4]
            expiration_date = line[5]
            data.append(id)
            data.append(date)
            data.append(product)
            data.append(buy_price)
            data.append(amount)
            data.append(expiration_date)
            tdata.append(data)

    t = Table(tdata)
    flow_obj.append(t)
    pdf.build(flow_obj)


make_pdf_report()
