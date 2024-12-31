from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure Google Gemini API with your API key
genai.configure(api_key="AIzaSyAE-fHL5yh8whzCLk3qbaMc4kjH3Zi-jfE")

# Route to serve the homepage (index.html)
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML frontend

# API route to handle user input and generate response from Google Gemini
@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Get the user's prompt from the request
        data = request.json
        prompt = data.get('prompt')

        # Validate the prompt
        if not prompt:
            return jsonify({"error": "No prompt provided"}), 400

        # Initialize the Google Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate content from the model based on the prompt
        response = model.generate_content(prompt)

        # Return the response to the frontend
        return jsonify({"response": response.text})

    except Exception as e:
        # Handle any errors and return them as a JSON response
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port,debug=True)
