import os

from google import genai
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# PocketWise categories
CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Education",
    "Other"
]


def local_fallback_category(description):
    """
    Simple backup categorization.

    This is used only when Gemini is temporarily unavailable.
    """

    text = description.lower()

    food_words = [
        "food", "lunch", "dinner", "breakfast",
        "biryani", "pizza", "burger", "restaurant",
        "snack", "coffee", "tea", "swiggy", "zomato"
    ]

    transport_words = [
        "uber", "ola", "bus", "train", "metro",
        "auto", "cab", "petrol", "fuel",
        "transport", "rickshaw"
    ]

    shopping_words = [
        "shirt", "dress", "clothes", "shopping",
        "shoes", "watch", "bag", "amazon",
        "flipkart", "purchase"
    ]

    entertainment_words = [
        "movie", "cinema", "netflix", "game",
        "gaming", "concert", "party", "entertainment"
    ]

    education_words = [
        "book", "textbook", "course", "college",
        "exam", "education", "notebook", "pen",
        "stationery", "tuition"
    ]


    if any(word in text for word in food_words):
        return "Food"

    if any(word in text for word in transport_words):
        return "Transport"

    if any(word in text for word in shopping_words):
        return "Shopping"

    if any(word in text for word in entertainment_words):
        return "Entertainment"

    if any(word in text for word in education_words):
        return "Education"

    return "Other"


def categorize_expense(description):

    prompt = f"""
You are the Expense Agent of PocketWise,
a student expense tracking application.

Categorize the following expense into exactly ONE
of these categories:

Food
Transport
Shopping
Entertainment
Education
Other

Expense description:
"{description}"

Return ONLY the category name.
Do not provide an explanation.
"""


    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        category = response.text.strip()


        # Check Gemini result
        for allowed_category in CATEGORIES:

            if category.lower() == allowed_category.lower():
                return allowed_category


        # If Gemini gives an unexpected answer
        return local_fallback_category(description)


    except Exception as error:

        # Gemini may temporarily return 503 or another
        # server/API error. Do not crash the website.

        print("Gemini Expense Agent unavailable:", error)
        print("Using local fallback categorization.")

        return local_fallback_category(description)