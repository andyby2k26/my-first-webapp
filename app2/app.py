import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

# Initialize Flask app
app = Flask(__name__)

# Load configuration from environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key_that_should_be_in_env_var')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and form handling
db = SQLAlchemy(app)

# ==================================
# 1. Database Model
# ==================================
# Define the Note model to match the app1_data table from your SQL script
class Note(db.Model):
    __tablename__ = 'app2_data'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False) # New column
    content = db.Column(db.Text, nullable=False)     # New column
    created_at = db.Column(db.TIMESTAMP(timezone=True), server_default=db.func.now())

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'

# ==================================
# 2. Form Class
# ==================================
# Define a form using Flask-WTF (no change needed here as fields were already named 'title' and 'content')
class NoteForm(FlaskForm):
    title = StringField('Note Title', validators=[DataRequired()])
    content = TextAreaField('Note Content', validators=[DataRequired()])
    submit = SubmitField('Save Note')

# ==================================
# 3. Flask Routes
# ==================================
@app.route('/')
def home():
    # Fetch all notes from the database to display them
    notes = db.session.execute(db.select(Note).order_by(Note.created_at.desc())).scalars().all()
    return render_template('index.html', notes=notes)

@app.route('/new-note', methods=['GET', 'POST'])
def new_note():
    form = NoteForm()
    
    # Check if the form was submitted and is valid
    if form.validate_on_submit():
        # Get data from the form
        note_title = form.title.data
        note_content = form.content.data
        
        # Create a new Note object with separate title and content
        new_note = Note(title=note_title, content=note_content)
        
        # Add the new note to the session and commit to the database
        db.session.add(new_note)
        db.session.commit()
        
        # Redirect back to the homepage to see the new note
        return redirect(url_for('home'))
        
    # If the form is not submitted or not valid, render the form page
    return render_template('new_note.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        # This will create tables if they don't exist.
        # For production, use a migration tool like Flask-Migrate.
        db.create_all()
    app.run(host='0.0.0.0', debug=True)