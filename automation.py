def calculate_priority(event_type, budget, guests):
    """
    Returns:
        score (int)
        priority (str)
    """

    score = 0

    # Event Type
    if event_type.lower() == "wedding":
        score += 20
    elif event_type.lower() == "corporate":
        score += 15
    elif event_type.lower() == "engagement":
        score += 10
    else:
        score += 5

    # Budget
    if budget >= 500000:
        score += 50
    elif budget >= 100000:
        score += 40
    elif budget >= 50000:
        score += 20
    else:
        score += 10

    # Guests
    if guests >= 300:
        score += 30
    elif guests >= 150:
        score += 20
    elif guests >= 50:
        score += 10

    # Priority
    if score >= 80:
        priority = "High"

    elif score >= 50:
        priority = "Medium"

    else:
        priority = "Low"

    return score, priority


def recommend_package(event_type, budget):

    event_type = event_type.lower()

    if event_type == "wedding":

        if budget >= 300000:
            return "Premium Wedding Package"

        return "Classic Wedding Package"

    elif event_type == "corporate":

        return "Corporate Elite Package"

    elif event_type == "birthday":

        return "Birthday Starter Package"

    elif event_type == "engagement":

        return "Engagement Celebration Package"

    return "Standard Event Package"


def generate_ai_message(name,
                        event_type,
                        guests,
                        package):

    return f"""
Hi {name},

Thank you for your enquiry.

Based on your {event_type} event for approximately {guests} guests, we recommend our {package}.

Our sales team will contact you shortly with pricing and availability.

Thank you for choosing LeadFlow AI.
""".strip()