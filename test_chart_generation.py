from database import get_all_leads
from charts import generate_all_charts

leads = get_all_leads()

generate_all_charts(leads)

print("Charts generated successfully!")