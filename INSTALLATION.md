🛠️ Installation & Execution Guide

📖 Prerequisites

Ensure you have the following installed:

* Python 3.x

* pip (Python package manager)

* A web browser (for chatbot UI)

🔧 Step 1: Clone the Repository

* git clone https://github.com/your-repo/cdp_chatbot.git
cd cdp_chatbot

🏃️ Step 2: Install Dependencies

* Run the following command to install required Python packages:

* pip install -r requirements.txt

If requirements.txt is missing, install manually:

* pip install flask fuzzywuzzy python-Levenshtein

🔄 Step 3: Run the Chatbot

Start the Flask application:

* python app.py

* The chatbot should now be running locally at: http://127.0.0.1:5000/

✅ Troubleshooting

* If styles are not applying, check browser cache and clear it.

* If Flask does not start, ensure app.py is in the project root and Python is correctly installed.

* If FuzzyWuzzy is not found, install python-Levenshtein manually: pip install python-Levenshtein

