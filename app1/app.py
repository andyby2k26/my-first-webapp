# Import the Flask class from the flask module
from flask import Flask, render_template, request, render_template
from datetime import datetime

# Create an instance of the Flask application
# The __name__ argument helps Flask locate resources like templates
app = Flask(__name__)

# Define a route for the home page ("/")
# When a user visits the root URL, this function will be executed
@app.route("/")
def home():
    current_time = datetime.now()
    # Render the 'index.html' template
    # Flask looks for templates in a 'templates' folder by default
    return render_template("index.html", current_time=current_time)

@app.route("/page", methods=["POST"])
def page():
    user_name = request.form.get("user_name")
    email = request.form.get("user_email")
    message = request.form.get("user_message")
    # Render the 'index.html' template
    # Flask looks for templates in a 'templates' folder by default
    return render_template("page.html", name=user_name, email=email, message=message)

# This block ensures the Flask development server runs only when the script is executed directly
if __name__ == "__main__":
    # Run the Flask application in debug mode
    # debug=True allows for automatic reloading on code changes and provides a debugger
    # host='0.0.0.0' makes the server accessible from any IP address,
    # which is useful for testing in a local network or Docker
    app.run(debug=True, host='0.0.0.0')
