from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # For flash messages

# Personal information
personal_info = {
    'name': 'Syed Wasi Shah',
    'title': 'Software Engineering Student',
    'semester': 'Semester 4',
    'email': 'wasi.officialll@gmail.com',
    'github': 'https://github.com',
    'linkedin': 'https://linkedin.com',
    'about': '''I'm a passionate software engineering student currently in my 4th semester. 
    I love building innovative solutions and learning new technologies. 
    My journey in software development focuses on creating efficient and user-friendly applications.''',
    'skills': [
        'Python', 'Java', 'HTML/CSS', 'JavaScript', 
        'SQL', 'Git', 'Flask', 'Data Structures'
    ],
    'projects': [
        {
            'name': 'Student Management System',
            'description': 'A web application to manage student records using Flask and Python.',
            'tech': 'Python, Flask, HTML, Bootstrap'
        },
        {
            'name': 'Portfolio Website',
            'description': 'Personal portfolio website showcasing skills and projects.',
            'tech': 'HTML, CSS, JavaScript'
        }
    ],
    'education': [
        {'institution': 'University of Technology', 'degree': 'BS Software Engineering', 'year': '2024 - Present', 'semester': 'Semester 4'}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', info=personal_info)

@app.route('/about')
def about():
    return render_template('about.html', info=personal_info)

@app.route('/projects')
def projects():
    return render_template('projects.html', info=personal_info)

@app.route('/contact')
def contact():
    return render_template('contact.html', info=personal_info)

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Email configuration
    # To get a Gmail App Password:
    # 1. Enable 2-Step Verification on your Google Account
    # 2. Go to Google Account > Security > App Passwords
    # 3. Create a new app password for "Mail" and "Other (Custom name)"
    # 4. Use the generated 16-character password below (NOT your regular password)
    sender_email = "wasi.officialll@gmail.com"  # Your Gmail
    # IMPORTANT: Replace this with your actual 16-character Gmail App Password
    # Do NOT use your regular Gmail password
    
    # Get password from environment variable or use the provided password
    sender_password = os.environ.get("GMAIL_APP_PASSWORD", "")
    
    # If no password is set in environment, use a default (replace with your actual 16-char app password)
    if not sender_password:
        # Replace this with your actual 16-character Gmail App Password
        # Example: "abcd efgh ijkl mnop" (without quotes)
        sender_password = "cpeu zqee dkzi sxmh"
    recipient_email = "wasi.officialll@gmail.com"
    
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Portfolio Contact: {name}"
        
        body = f"""
New message from your portfolio website!

Name: {name}
Email: {email}

Message:
{message}
"""
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        
        flash('Message sent successfully! I will get back to you soon.', 'success')
    except Exception as e:
        # Log the error for debugging
        print(f"Error sending email: {str(e)}")
        flash(f'Error sending message. Please try again or email me directly.', 'error')
    
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
