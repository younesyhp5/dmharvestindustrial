from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'harvestindustry480@gmail.com'
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Validate form fields (add more validation as needed)
    if not name or not email or not message:
        flash('All fields are required!', 'danger')
        return redirect(url_for('contact'))

    # Send email
    msg = Message('New Contact Form Submission',
                  sender='your_email@example.com',
                  recipients=['your_email@example.com'])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    try:
        mail.send(msg)
        flash('Message sent successfully!', 'success')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'danger')

    return redirect(url_for('contact'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)