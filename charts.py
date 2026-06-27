from collections import Counter
import os
import matplotlib.pyplot as plt


STATIC_FOLDER = "static"


def calculate_kpis(leads):

    total_leads = len(leads)

    total_revenue = sum(lead[6] for lead in leads)

    average_budget = (
        total_revenue / total_leads
        if total_leads else 0
    )

    high_priority = sum(
        1 for lead in leads
        if lead[9] == "High"
    )

    pending = sum(
        1 for lead in leads
        if lead[12] == "Pending"
    )

    contacted = sum(
        1 for lead in leads
        if lead[12] == "Contacted"
    )

    closed = sum(
        1 for lead in leads
        if lead[12] == "Closed"
    )

    return {

        "total_leads": total_leads,
        "total_revenue": total_revenue,
        "average_budget": round(average_budget, 2),
        "high_priority": high_priority,
        "pending": pending,
        "contacted": contacted,
        "closed": closed

    }


def event_distribution(leads):

    events = [
        lead[4]
        for lead in leads
    ]

    return dict(Counter(events))


def priority_distribution(leads):

    priorities = [
        lead[9]
        for lead in leads
        if lead[9] != ""
    ]

    return dict(Counter(priorities))


# -----------------------------
# Generate Pie Chart
# -----------------------------

def generate_event_chart(leads):

    data = event_distribution(leads)

    if not data:
        return

    plt.figure(figsize=(6,6))

    plt.pie(
        data.values(),
        labels=data.keys(),
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Event Distribution")

    os.makedirs(STATIC_FOLDER, exist_ok=True)

    plt.savefig(
        os.path.join(
            STATIC_FOLDER,
            "event_distribution.png"
        )
    )

    plt.close()


# -----------------------------
# Generate Bar Chart
# -----------------------------

def generate_priority_chart(leads):

    data = priority_distribution(leads)

    if not data:
        return

    plt.figure(figsize=(6,4))

    plt.bar(
        data.keys(),
        data.values()
    )

    plt.title("Priority Distribution")

    plt.xlabel("Priority")

    plt.ylabel("Leads")

    os.makedirs(STATIC_FOLDER, exist_ok=True)

    plt.savefig(
        os.path.join(
            STATIC_FOLDER,
            "priority_distribution.png"
        )
    )

    plt.close()


# -----------------------------
# Generate All Charts
# -----------------------------

def generate_all_charts(leads):

    generate_event_chart(leads)

    generate_priority_chart(leads)