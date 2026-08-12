def calculate_savings(analysis_result, monthly_income):
    """
    Savings Agent

    Receives:
    1. Monthly income
    2. Total spending calculated by the Analysis Agent

    Calculates the amount remaining after expenses.
    """

    total_spending = analysis_result["total"]

    monthly_income = float(monthly_income)

    available_savings = monthly_income - total_spending

    # Prevent negative savings
    if available_savings < 0:
        available_savings = 0


    # Calculate percentage of income remaining
    if monthly_income > 0:

        savings_rate = (
            available_savings / monthly_income
        ) * 100

    else:

        savings_rate = 0


    if available_savings == 0:

        message = (
            "Your current expenses are equal to or greater "
            "than your monthly income. Focus on reducing "
            "expenses before starting a SIP."
        )

    else:

        message = (
            f"Your monthly income is ₹{monthly_income:.2f} "
            f"and your total spending is ₹{total_spending:.2f}. "
            f"You have approximately ₹{available_savings:.2f} "
            f"available after your expenses."
        )


    return {

        "monthly_income": monthly_income,

        "total_spending": total_spending,

        "available_savings": available_savings,

        "savings_rate": savings_rate,

        "message": message

    }