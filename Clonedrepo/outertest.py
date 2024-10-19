from flask import Flask, request, jsonify, render_template
import aiml
import os

# Create Flask app
app = Flask(__name__)

# Create a kernel object
kernel = aiml.Kernel()

# Load AIML files
aiml_file = "aiml/aiml_bot.aiml"
if os.path.exists(aiml_file):
    kernel.learn(aiml_file)
else:
    print(f"AIML file not found: {aiml_file}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message')
    response = kernel.respond(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
