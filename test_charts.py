from database import get_all_leads
from charts import *

leads = get_all_leads()

print()

print(calculate_kpis(leads))

print()

print(event_distribution(leads))

print()

print(priority_distribution(leads))