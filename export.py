import csv
import os

from openpyxl import Workbook


EXPORT_FOLDER = "exports"


def create_export_folder():
    os.makedirs(EXPORT_FOLDER, exist_ok=True)


def export_csv(leads):

    create_export_folder()

    filepath = os.path.join(
        EXPORT_FOLDER,
        "leads.csv"
    )

    with open(
        filepath,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Name",
            "Phone",
            "Email",
            "Event",
            "Guests",
            "Budget",
            "Event Date",
            "Requirements",
            "Priority",
            "Package",
            "AI Message",
            "Status",
            "Created At"
        ])

        for lead in leads:
            writer.writerow(lead)

    return filepath


def export_excel(leads):

    create_export_folder()

    workbook = Workbook()

    sheet = workbook.active

    sheet.title = "Leads"

    sheet.append([
        "ID",
        "Name",
        "Phone",
        "Email",
        "Event",
        "Guests",
        "Budget",
        "Event Date",
        "Requirements",
        "Priority",
        "Package",
        "AI Message",
        "Status",
        "Created At"
    ])

    for lead in leads:
        sheet.append(list(lead))

    filepath = os.path.join(
        EXPORT_FOLDER,
        "leads.xlsx"
    )

    workbook.save(filepath)

    return filepath