from flask import Flask, render_template, request, redirect, jsonify

from database.database import (
    initialize_database,
    add_expense,
    get_expenses
)

from agents.expense_agent import categorize_expense
from agents.workflow import run_multi_agent_workflow


app = Flask(__name__)


# =========================================================
# INITIALIZE DATABASE
# =========================================================

initialize_database()


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")
def home():

    expenses = get_expenses()

    return render_template(
        "index.html",
        expenses=expenses
    )


# =========================================================
# ADD EXPENSE
# =========================================================

@app.route("/add-expense", methods=["POST"])
def add_new_expense():

    description = request.form.get("description")
    amount = request.form.get("amount")

    if description and amount:

        # -----------------------------------------
        # EXPENSE AGENT
        # -----------------------------------------

        category = categorize_expense(description)

        # -----------------------------------------
        # SAVE EXPENSE
        # -----------------------------------------

        add_expense(
            description=description,
            amount=float(amount),
            category=category
        )

    return redirect("/")


# =========================================================
# MULTI-AGENT ANALYSIS
# =========================================================

@app.route("/analyze", methods=["GET"])
def analyze():

    # Get monthly income from the website
    monthly_income = request.args.get(
        "monthly_income",
        type=float
    )


    # Make sure income was provided
    if monthly_income is None or monthly_income <= 0:

        return jsonify({
            "error": "Please provide a valid monthly income."
        }), 400


    # Get all expenses
    expenses = get_expenses()


    # Run the complete multi-agent workflow
    result = run_multi_agent_workflow(
        expenses,
        monthly_income
    )


    return jsonify(result)


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)