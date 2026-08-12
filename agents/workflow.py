from agents.analysis_agent import analyze_expenses
from agents.savings_agent import calculate_savings
from agents.investment_agent import suggest_investment


def run_multi_agent_workflow(expenses, monthly_income):
    """
    PocketWise Multi-Agent Workflow

    Agent communication:

    Expense Agent
          ↓
    Analysis Agent
          ↓
    Savings Agent
          ↓
    Investment Agent
    """

    # --------------------------------------------------
    # AGENT 1
    # Expense Agent
    #
    # Expenses have already been categorized when
    # they were added to the database.
    # --------------------------------------------------

    categorized_expenses = expenses


    # --------------------------------------------------
    # AGENT 2
    # Analysis Agent
    # --------------------------------------------------

    analysis_result = analyze_expenses(
        categorized_expenses
    )


    # --------------------------------------------------
    # AGENT 3
    # Savings Agent
    #
    # Receives BOTH:
    # - Analysis result
    # - Monthly income
    # --------------------------------------------------

    savings_result = calculate_savings(
        analysis_result,
        monthly_income
    )


    # --------------------------------------------------
    # AGENT 4
    # Investment Agent
    # --------------------------------------------------

    investment_result = suggest_investment(
        savings_result
    )


    # --------------------------------------------------
    # FINAL RESULT
    # --------------------------------------------------

    return {

        "analysis": analysis_result,

        "savings": savings_result,

        "investment": investment_result

    }