from collections import defaultdict


def analyze_expenses(expenses):
    """
    Analysis Agent

    Receives categorized expenses from the Expense Agent
    and identifies spending patterns.
    """

    category_totals = defaultdict(float)

    total_spending = 0

    for expense in expenses:

        category = expense["category"]
        amount = float(expense["amount"])

        category_totals[category] += amount
        total_spending += amount


    # No expenses
    if total_spending == 0:

        return {
            "total": 0,
            "category_totals": {},
            "top_category": "None",
            "top_amount": 0,
            "top_percentage": 0,
            "message": "Add some expenses to receive spending analysis."
        }


    # Find highest spending category
    top_category = max(
        category_totals,
        key=category_totals.get
    )

    top_amount = category_totals[top_category]

    top_percentage = (
        top_amount / total_spending
    ) * 100


    message = (
        f"Your highest spending category is "
        f"{top_category}, accounting for "
        f"{top_percentage:.1f}% of your total spending."
    )


    return {
        "total": total_spending,
        "category_totals": dict(category_totals),
        "top_category": top_category,
        "top_amount": top_amount,
        "top_percentage": top_percentage,
        "message": message
    }