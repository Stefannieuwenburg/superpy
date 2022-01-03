from reportlab.platypus import SimpleDocTemplate, Table
import csv


def export_to_pdf():
    pdf = SimpleDocTemplate("report.pdf")
    flow_obj = []

    with open("bought.csv", "r") as f:
        bought_report = csv.reader(f)
        tdata = []
        for line in bought_report:
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


export_to_pdf()
