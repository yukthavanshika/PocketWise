// =========================================================
// POCKETWISE - FRONTEND JAVASCRIPT
// =========================================================


// =========================================================
// MONTHLY INCOME
// =========================================================

const incomeInput =
    document.getElementById("monthly-income");

const incomeDisplay =
    document.getElementById("monthly-income-display");


if (incomeInput) {

    const savedIncome =
        localStorage.getItem("pocketwise_income");

    if (savedIncome) {

        incomeInput.value = savedIncome;

        updateIncomeDisplay(savedIncome);

    }


    incomeInput.addEventListener(
        "input",
        function () {

            const income =
                incomeInput.value;

            localStorage.setItem(
                "pocketwise_income",
                income
            );

            updateIncomeDisplay(income);

        }
    );

}


function updateIncomeDisplay(income) {

    if (!incomeDisplay) {
        return;
    }


    const value =
        parseFloat(income);


    if (isNaN(value)) {

        incomeDisplay.textContent =
            "₹0";

        return;

    }


    incomeDisplay.textContent =
        "₹" + value.toFixed(2);

}



// =========================================================
// ANALYZE BUTTON
// =========================================================

const analyzeButton =
    document.getElementById("analyze-button");


if (analyzeButton) {

    analyzeButton.addEventListener(
        "click",
        async function () {


            const incomeInput =
                document.getElementById(
                    "monthly-income"
                );


            const monthlyIncome =
                parseFloat(
                    incomeInput.value
                );


            if (
                isNaN(monthlyIncome) ||
                monthlyIncome <= 0
            ) {

                alert(
                    "Please enter your monthly income first."
                );

                incomeInput.focus();

                return;

            }


            localStorage.setItem(
                "pocketwise_income",
                monthlyIncome
            );


            analyzeButton.disabled =
                true;

            analyzeButton.innerHTML =
                "🤖 Agents are analyzing...";


            try {

                const response =
                    await fetch(
                        "/analyze?monthly_income=" +
                        encodeURIComponent(
                            monthlyIncome
                        )
                    );


                if (!response.ok) {

                    throw new Error(
                        "Server returned an error."
                    );

                }


                const result =
                    await response.json();


                // =========================================
                // ANALYSIS AGENT
                // =========================================

                const analysis =
                    result.analysis;


                document.getElementById(
                    "analysis-result"
                ).textContent =
                    analysis.message;


                // =========================================
                // UPDATE ALL CATEGORY INFORMATION
                // =========================================

                updateSpendingOverview(
                    analysis.category_totals,
                    analysis.total
                );


                // =========================================
                // SAVINGS AGENT
                // =========================================

                const savings =
                    result.savings;


                document.getElementById(
                    "saving-result"
                ).textContent =
                    savings.message;


                document.getElementById(
                    "potential-savings"
                ).textContent =
                    "₹" +
                    savings.available_savings.toFixed(2);


                // =========================================
                // INVESTMENT AGENT
                // =========================================

                const investment =
                    result.investment;


                document.getElementById(
                    "investment-result"
                ).textContent =
                    investment.message;


                // =========================================
                // SUCCESS
                // =========================================

                analyzeButton.innerHTML =
                    "✓ Analysis Complete";


            } catch (error) {

                console.error(
                    "Multi-agent analysis error:",
                    error
                );


                analyzeButton.innerHTML =
                    "⚠️ Analysis Failed";


                alert(
                    "Unable to analyze expenses. " +
                    "Please make sure the Flask server is running."
                );

            }


            setTimeout(
                function () {

                    analyzeButton.disabled =
                        false;

                    analyzeButton.innerHTML =
                        "🤖 Analyze My Expenses";

                },
                2500
            );

        }
    );

}



// =========================================================
// UPDATE SPENDING OVERVIEW
// =========================================================

function updateSpendingOverview(
    categoryTotals,
    total
) {


    // ---------------------------------------------
    // CATEGORY LIST
    // ---------------------------------------------

    const categories = [
        "Food",
        "Transport",
        "Shopping",
        "Entertainment",
        "Education"
    ];


    categories.forEach(
        function (category) {


            const amount =
                categoryTotals[category] || 0;


            // -----------------------------------------
            // Update percentage
            // -----------------------------------------

            let percentage = 0;


            if (total > 0) {

                percentage =
                    (amount / total) * 100;

            }


            const categoryId =
                category.toLowerCase();


            const percentElement =
                document.getElementById(
                    categoryId +
                    "-percent"
                );


            const barElement =
                document.getElementById(
                    categoryId +
                    "-bar"
                );


            if (percentElement) {

                percentElement.textContent =
                    percentage.toFixed(1) +
                    "%";

            }


            if (barElement) {

                barElement.style.width =
                    Math.min(
                        percentage,
                        100
                    ) +
                    "%";

            }


            // -----------------------------------------
            // Update summary card amounts
            // -----------------------------------------

            const summaryElement =
                document.getElementById(
                    categoryId +
                    "-spending"
                );


            if (summaryElement) {

                summaryElement.textContent =
                    "₹" +
                    amount.toFixed(2);

            }

        }
    );

}



// =========================================================
// UPDATE OVERVIEW ON PAGE LOAD
// =========================================================
//
// This gets the current expense data from the server
// and updates the dashboard immediately.
// =========================================================

async function loadCurrentOverview() {

    try {

        const response =
            await fetch("/analyze?monthly_income=1");


        if (!response.ok) {
            return;
        }


        const result =
            await response.json();


        if (
            result &&
            result.analysis
        ) {

            const analysis =
                result.analysis;


            updateSpendingOverview(
                analysis.category_totals,
                analysis.total
            );

        }

    } catch (error) {

        console.log(
            "Initial overview will use server data."
        );

    }

}


// Run when page loads
loadCurrentOverview();