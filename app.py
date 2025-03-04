from flask import Flask, render_template, request, jsonify
import json
from fuzzywuzzy import process

app = Flask(__name__, static_folder="static")


# Load knowledge base from JSON
with open("cdp_data.json", "r") as f:
    knowledge_base = json.load(f)

def find_best_match(user_question):
    """Find the best-matching question from the knowledge base."""
    possible_questions = []
    mappings = {}

    # Extract all possible questions
    for cdp, data in knowledge_base.items():
        for question, answer in data.items():
            possible_questions.append(question)
            mappings[question] = answer  # Store answer mapping

    # Perform fuzzy matching
    best_match, score = process.extractOne(user_question, possible_questions)
    
    if score >= 75:  # Acceptable threshold
        return mappings[best_match]
    
    return "I'm sorry, I couldn't find relevant information. Please check the official documentation."

@app.route("/")
def index():
    """Render the chatbot UI."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Process user input and return the chatbot's response."""
    data = request.json
    user_question = data.get("question", "").strip()

    if not user_question:
        return jsonify({"error": "No question provided."})

    answer = find_best_match(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
