from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    send_file
)

from database import (
    init_db,
    insert_lead,
    get_all_leads,
    get_lead,
    update_status,
    delete_lead
)

from automation import (
    calculate_priority,
    recommend_package,
    generate_ai_message
)

from charts import (
    calculate_kpis,
    event_distribution,
    priority_distribution,
    generate_all_charts
)

from export import (
    export_csv,
    export_excel
)

app = Flask(__name__)

# ============================================
# Initialize Database
# ============================================

init_db()


# ============================================
# HOME
# ============================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================
# SUBMIT NEW LEAD
# ============================================

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    event_type = request.form["event_type"]

    guests = int(request.form["guests"])
    budget = int(request.form["budget"])

    event_date = request.form["event_date"]
    requirements = request.form["requirements"]

    score, priority = calculate_priority(
        event_type,
        budget,
        guests
    )

    package = recommend_package(
        event_type,
        budget
    )

    ai_message = generate_ai_message(
        name,
        event_type,
        guests,
        package
    )

    insert_lead(
        name,
        phone,
        email,
        event_type,
        guests,
        budget,
        event_date,
        requirements,
        priority,
        package,
        ai_message,
        "Pending"
    )

    return redirect(url_for("dashboard"))


# ============================================
# DASHBOARD
# ============================================

@app.route("/dashboard")
def dashboard():

    leads = get_all_leads()

    return render_template(
        "dashboard.html",
        leads=leads,
        total=len(leads)
    )


# ============================================
# LEAD DETAILS
# ============================================

@app.route("/lead/<int:lead_id>")
def lead_details(lead_id):

    lead = get_lead(lead_id)

    return render_template(
        "lead.html",
        lead=lead
    )


# ============================================
# UPDATE STATUS
# ============================================

@app.route("/contacted/<int:lead_id>")
def contacted(lead_id):

    update_status(
        lead_id,
        "Contacted"
    )

    return redirect(
        url_for(
            "lead_details",
            lead_id=lead_id
        )
    )


@app.route("/closed/<int:lead_id>")
def closed(lead_id):

    update_status(
        lead_id,
        "Closed"
    )

    return redirect(
        url_for(
            "lead_details",
            lead_id=lead_id
        )
    )


# ============================================
# DELETE LEAD
# ============================================

@app.route("/delete/<int:lead_id>")
def delete(lead_id):

    delete_lead(lead_id)

    return redirect(url_for("dashboard"))


# ============================================
# ANALYTICS
# ============================================

@app.route("/analytics")
def analytics():

    leads = get_all_leads()

    # Regenerate charts every visit
    generate_all_charts(leads)

    kpis = calculate_kpis(leads)

    events = event_distribution(leads)

    priorities = priority_distribution(leads)

    return render_template(
        "analytics.html",
        kpis=kpis,
        events=events,
        priorities=priorities
    )


# ============================================
# EXPORT CSV
# ============================================

@app.route("/export/csv")
def download_csv():

    leads = get_all_leads()

    filepath = export_csv(leads)

    return send_file(
        filepath,
        as_attachment=True,
        download_name="LeadFlowAI_Leads.csv"
    )


# ============================================
# EXPORT EXCEL
# ============================================

@app.route("/export/excel")
def download_excel():

    leads = get_all_leads()

    filepath = export_excel(leads)

    return send_file(
        filepath,
        as_attachment=True,
        download_name="LeadFlowAI_Leads.xlsx"
    )


# ============================================
# RUN APPLICATION
# ============================================

if __name__ == "__main__":
    app.run(debug=True)