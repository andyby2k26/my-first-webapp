# app1/app.py
# The boilerplate Flask application for App 1.
# It has a main route '/' and a secondary route '/about'.
# Now uses url_for to generate links, which will correctly prepend the
# SCRIPT_NAME provided by Nginx.
# Imported ProxyFix to correctly handle proxy headers.
from flask import Flask, render_template_string, url_for, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__, static_folder='images')
# Apply ProxyFix to the Flask app to correctly handle forwarded headers
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

@app.route('/')
def index():
    """Renders the main page for App1."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page for App1."""
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>App1 About</title>
            <style>
                body { font-family: sans-serif; margin: 20px; background-color: #f0f8ff; color: #333; }
                h1 { color: #4682b4; }
                a { color: #1e90ff; text-decoration: none; }
                a:hover { text-decoration: underline; }
                div { background-color: #e0f2f7; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            </style>
        </head>
        <body>
            <div>
                <h1>About App1</h1>
                <p>This is the about page for App1, demonstrating internal routing.</p>
                <p>Go back to the main page:</p>
                <a href="{{ url_for('index') }}">Go back to Home (internal link)</a>
            </div>
        </body>
        </html>
    ''')

@app.route('/ellie')
def ellie():
    """Renders the about page for App1."""
    return render_template('ellie.html')

@app.route('/sam')
def sam():
    """Renders the about page for App1."""
    return render_template('sam.html')

if __name__ == '__main__':
    # When running locally (outside Docker), use this.
    # Inside Docker, Gunicorn handles the serving.
    app.run(debug=True,host='0.0.0.0', port=5000)
