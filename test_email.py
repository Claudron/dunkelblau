from flask import Flask
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

def send_test_email():
    with app.app_context():
        msg = Message(subject='Hello',
                      sender='your-email@example.com',
                      recipients=['recipient@example.com'])
        msg.body = 'This is a other test email sent from a Flask app'
        mail.send(msg)
        print('Email sent!')

if __name__ == '__main__':
    send_test_email()
