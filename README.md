💰 PocketWise – AI-Powered Student Expense Tracker

PocketWise is an AI-powered personal expense tracking application designed especially for students. It helps users record daily expenses, categorize spending, analyze financial habits, and receive personalized savings and basic investment suggestions.

The project combines a simple web interface with AI-powered agents to make expense management easier, smarter, and more personalised.

🎯 Objectives

Track daily expenses easily.

Automatically categorise expenses using AI.

Analyse spending patterns.

Calculate total spending and savings percentage.

Provide personalised savings suggestions.

Provide basic investment suggestions for educational purposes.

Help students develop better financial habits.

✨ Features

📝 Expense Tracking

Users can add expenses with:

Description

Amount

Category

Date

🤖 AI Expense Categorisation

The AI agent analyses an expense description and assigns an appropriate category.

Examples:

Lunch at restaurant → Food

Bought a new shirt → Shopping

Uber to college → Transportation

📊 Expense Analysis

PocketWise analyses spending and provides:

Total expenses

Category-wise spending

Spending patterns

Savings percentage

💡 Savings Suggestions

The system provides suggestions based on spending behaviour to help users reduce unnecessary expenses and improve savings.

📈 Investment Suggestions

PocketWise provides basic, educational investment suggestions based on the user's spending and savings information.

Investment suggestions are for educational purposes only and are not professional financial advice.

🧠 AI Agents

The project uses AI-powered components for:

Expense categorization

Expense analysis

Savings recommendations

Investment suggestions

🛠️ Technology Stack

Frontend

HTML

CSS

JavaScript

Jinja2 Templates

Backend

Python

Flask

Database

SQLite

AI

Google Gemini API

Google GenAI Python SDK

Tools

VS Code

Git

GitHub

Deployment

Render

🏗️ Application Workflow

User enters an expense
        ↓
Flask receives the expense
        ↓
AI categorises the expense
        ↓
Expense is stored in SQLite
        ↓
Spending data is analysed
        ↓
Savings/investment suggestions are generated
        ↓
Results are displayed to the user

📁 Project Structure

PocketWise/
│
├── agents/
│   └── AI agent modules
│
├── database/
│   └── database.py
│
├── static/
│   └── CSS / JavaScript / static assets
│
├── templates/
│   └── HTML templates
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

⚙️ Installation

1. Clone the repository

git clone https://github.com/mvrahul12/PocketWise.git
cd PocketWise

2. Create a virtual environment

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

Windows:

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

🔑 API Key Configuration

PocketWise uses the Google Gemini API for AI-powered functionality.

Set your API key as an environment variable. For example:

GOOGLE_API_KEY=your_api_key_here

If the project uses a .env file locally, create it in the project root.

Never upload API keys, passwords, or other secrets to GitHub.

▶️ Run the Application

Start the Flask application:

python app.py

Then open:

http://127.0.0.1:5000

in your browser.

🚀 Deployment

PocketWise can be deployed as a Flask web application using a platform such as Render.

The production start command is:

gunicorn app:app

Required dependencies should be included in requirements.txt.

🧪 Example

Input

Description: Lunch at restaurant
Amount: ₹250

AI Categorization

Category: Food

Analysis

Total Expenses: ₹2,500
Savings Percentage: 25%

The application can then generate suggestions based on the user's spending behavior.

🔮 Future Enhancements

User authentication and profiles

Interactive financial dashboards

Monthly and yearly reports

Budget planning

Financial goal tracking

Expense prediction

PostgreSQL support for persistent production data

Mobile application

Personalized notifications

Advanced financial analytics

🎓 Project Information

Project Name: PocketWise – AI-Powered Student Expense Tracker

Domain: Artificial Intelligence / Agentic AI / FinTech

Technologies: Python, Flask, SQLite, Google Gemini, HTML, CSS, JavaScript

👨‍💻 Contributors

Developed as an academic project demonstrating the use of AI-powered agents for personal expense management and financial awareness.

📄 License

This project is developed for educational and academic purposes.
