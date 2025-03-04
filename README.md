🌟 Support Agent Chatbot for Customer Data Platforms (CDPs)

📝 Project Overview:

This project is a web-based chatbot designed to assist users with "how-to" questions related to four major Customer Data Platforms (CDPs):

* Segment

* mParticle

* Lytics

* Zeotap

The chatbot extracts relevant information from the official documentation of these platforms to guide users in performing tasks such as setting up a source, creating user profiles, building audience segments, and integrating data.

🎯 Objective:

  The goal of this chatbot is to provide quick and accurate responses to users' technical queries about CDPs, making it easier for them to navigate the platforms without manually searching through documentation.

🛠️ Key Features:

✅ 1. Answer "How-to" Questions

Users can ask questions like:

"How do I set up a new source in Segment?"

"How can I create a user profile in mParticle?"

The chatbot extracts the most relevant answer from the documentation.

✅ 2. Intelligent Question Matching

Uses fuzzy matching to handle variations in user questions.

Ensures accurate responses even if the phrasing differs slightly.

✅ 3. Web-Based UI

Built with Flask (Python backend) and HTML/CSS (frontend) for a user-friendly experience.

Users can interact via a chat-style interface.

✅ 4. Error Handling & Response Optimization

If the chatbot cannot find an answer, it prompts users to check official documentation.

Filters out unrelated questions (e.g., "Which movie is releasing this week?").

✅ 5. Responsive & Mobile-Friendly Design

Ensures a smooth user experience across PCs, tablets, and smartphones.

✅ 6. Easy-to-Update Knowledge Base

Stores predefined answers in a JSON-based knowledge base for easy modifications.

Future versions may support real-time web scraping for updated answers.

🚀 Future Enhancements

👉 Live Data Extraction: Scraping the official documentation instead of using a static JSON file.👉 CDP Comparisons: Answering questions like "How does Segment compare to Lytics?".👉 Advanced NLP: Using embeddings or FAISS to improve question handling.

🛠️ Tech Stack

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Data Processing: JSON, FuzzyWuzzy (for text matching)

Deployment: Localhost (can be deployed on cloud platforms like Vercel/Heroku)

📂 Project Structure

/cdp_chatbot
│── /static
│   ├── styles.css         # Chatbot styling
│── /templates
│   ├── index.html         # Chatbot UI
│── app.py                 # Flask backend logic
│── cdp_data.json          # Knowledge base for CDP queries
│── README.md              # Project documentation
│── INSTALLATION.md        # Setup and execution steps



