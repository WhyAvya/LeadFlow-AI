from collections import Counter


def calculate_kpis(leads):
    """
    Calculates dashboard KPIs from all leads.
    """

    total_leads = len(leads)

    total_revenue = sum(
        lead[6] for lead in leads
    )

    average_budget = 0

    if total_leads > 0:
        average_budget = total_revenue / total_leads

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

        "average_budget": round(
            average_budget,
            2
        ),

        "high_priority": high_priority,

        "pending": pending,

        "contacted": contacted,

        "closed": closed

    }


def event_distribution(leads):
    """
    Counts leads by event type.
    """

    events = [
        lead[4]
        for lead in leads
    ]

    return dict(
        Counter(events)
    )


def priority_distribution(leads):
    """
    Counts High / Medium / Low.
    """

    priorities = [
        lead[9]
        for lead in leads
    ]

    return dict(
        Counter(priorities)
    )