from flat import Bill, Flatmate
from reports import PdfReport

bill_amount = float(input("Enter bill amount: "))
bill_period = input("Enter bill period: ")

flatmate1_name = input("Enter flatmate1 name: ")
flatmate1_days_in_house = float(input("Enter flatmate1 days in house: "))

flatmate2_name = input("Enter flatmate2 name: ")
flatmate2_days_in_house = float(input("Enter flatmate2 days in house: "))

bill = Bill(bill_amount, bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days_in_house)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days_in_house)

print(f"{flatmate1.name} pays: ", flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(filename=f"{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)

