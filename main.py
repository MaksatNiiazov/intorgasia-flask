from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message
import config
import requests

app = Flask(__name__)

app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mn25260518@gmail.com'
app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)

bot_token = config.TOKEN
chat_id = '-976199658'

class ContactForm(FlaskForm):
    name = StringField('Имя', render_kw={"placeholder": "Введите Ваше имя"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Ваш номер телефона"}, validators=[DataRequired()])
    message = TextAreaField('Message', render_kw={"placeholder": "По какому вопросу Вы хотите получить консультацию?"})
    submit = SubmitField('Купить', render_kw={"value": "Отправить", "class": "submit_button"} )

def send_telegram_message(chat_id, message_text):
    try:
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id': chat_id, 'text': message_text}
        response = requests.post(url, data=data)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error sending Telegram message: {e}")
        return False

def send_email(subject, sender, recipients, body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body

    try:
        mail.send(msg)
        return True
    except Exception as e:
        print(str(e))
        return False

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        if not form.message.data:
            form.message.data = 'Без сообщения.'
        message_text = f"{form.name.data} ({form.phone.data})\nСообщение:\n{form.message.data}"
        send_telegram_message(chat_id, message_text)
        recipients = ['mn25260518@gmail.com', 'intorgasia@gmail.com', 'niyazov37@gmail.com']
        if send_email('Заявка', 'mn25260518@gmail.com', recipients, message_text):
            flash('Заказ оформлен!', 'success')
        else:
            flash('Ошибка при отправке заказа.', 'error')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = ContactForm()
    return render_template('calculator.html', form=form)

if __name__ == '__main__':
    app.run(debug=False)
