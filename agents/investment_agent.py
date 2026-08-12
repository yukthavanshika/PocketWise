def suggest_investment(savings_result):
    """
    Investment Agent

    Receives available savings from the Savings Agent
    and suggests a simple SIP allocation.
    """

    available_savings = savings_result["available_savings"]

    # --------------------------------------------------
    # Keep part of the savings as a buffer and use
    # part for a possible SIP.
    # --------------------------------------------------

    suggested_sip = available_savings * 0.50

    emergency_buffer = (
        available_savings - suggested_sip
    )


    # --------------------------------------------------
    # Choose a simple SIP approach
    # --------------------------------------------------

    if available_savings < 500:

        category = "Build Savings First"

        suggestion = (
            "Your available savings are currently small. "
            "Focus on building a savings and emergency buffer "
            "before starting a SIP."
        )


    elif available_savings < 2000:

        category = "Small Diversified SIP"

        suggestion = (
            "Consider starting with a small SIP in a "
            "diversified or index-oriented mutual fund category. "
            "Only invest an amount you can comfortably maintain."
        )


    else:

        category = "Diversified / Index SIP"

        suggestion = (
            "You could consider a diversified or index-oriented "
            "mutual fund SIP using part of your available savings. "
            "Keeping the remaining amount as a financial buffer "
            "can help with unexpected expenses."
        )


    # --------------------------------------------------
    # Final message
    # --------------------------------------------------

    message = (
        f"Available savings: ₹{available_savings:.2f}. "
        f"Suggested SIP amount: ₹{suggested_sip:.2f}. "
        f"Suggested buffer: ₹{emergency_buffer:.2f}. "
        f"Approach: {suggestion}"
    )


    return {

        "category": category,

        "available_savings": available_savings,

        "suggested_sip": suggested_sip,

        "emergency_buffer": emergency_buffer,

        "suggestion": suggestion,

        "message": message

    }