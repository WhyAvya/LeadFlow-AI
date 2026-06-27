from database import get_all_leads
from export import export_csv, export_excel

leads = get_all_leads()

csv_file = export_csv(leads)
excel_file = export_excel(leads)

print(csv_file)
print(excel_file)

print("Export successful!")