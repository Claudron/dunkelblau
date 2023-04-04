from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# configure Flask-Mail with your email server settings
app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '59716b937de272'
app.config['MAIL_PASSWORD'] = '76542f00ee4401'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email():
    subject = request.form['subject']
    sender = request.form['sender']
    recipient = request.form['recipient']
    body = request.form['body']
    msg = Message(subject=subject,
                  sender=sender,
                  recipients=[recipient])
    msg.body = body
    mail.send(msg)
    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)
