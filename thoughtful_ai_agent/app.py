from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = {
    "questions": [
        {"question": "What does the eligibility verification agent (EVA) do?", 
         "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."},
        {"question": "What does the claims processing agent (CAM) do?", 
         "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."},
        {"question": "How does the payment posting agent (PHIL) work?", 
         "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."},
        {"question": "Tell me about Thoughtful AI's Agents.", 
         "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."},
        {"question": "What are the benefits of using Thoughtful AI's agents?", 
         "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = "Sorry, I don't have an answer to that question."

    for item in data['questions']:
        if user_input.lower() in item['question'].lower():
            response = item['answer']
            break
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify

faq_data = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to the Thoughtful AI Customer Support Agent! Ask me a question.'


@app.route('/ask', methods=['GET'])
def ask():
    user_query = request.args.get('question', '').lower()

    for item in faq_data:
        if user_query in item["question"].lower():
            return jsonify({"answer": item["answer"]})

    return jsonify({"answer": "Sorry, I don't have an answer to that. Could you please ask something else?"})


if __name__ == '__main__':
    app.run(debug=True)

