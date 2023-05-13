from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_mail import Mail, Message

import telegram

app = Flask(__name__)

app.config['SECRET_KEY'] = ''
app.config['MAIL_SERVER'] = 'smtp.yandex.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sitew3b@yandex.ru'  
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

bot = telegram.Bot(token='')

chat_id = '1105812455'


class ContactForm(FlaskForm):
    name = StringField('Имя', render_kw={"placeholder": "Введите Ваше имя"}, validators=[DataRequired()])
    phone = StringField('Phone', render_kw={"placeholder": "Ваш номер телефона"}, validators=[DataRequired()])
    message = TextAreaField('Message', render_kw={"placeholder": "Ваше сообщение"})
    submit = SubmitField('Купить', render_kw={"value": "Отправить", "class": "submit_button"} )


@app.route('/', methods=['GET', 'POST'])
async def index():
    form = ContactForm()
    if form.validate_on_submit():
        if not form.message:
            form.message.data = ''
        message_text = f"""{form.name.data} ({form.phone.data})
{form.message.data}"""
        await bot.send_message(chat_id=chat_id, text=message_text)
        msg = Message('New message from your website', sender='sitew3b@yandex.ru',
                      recipients=['sitew3b@yandex.ru'])
        msg.body = message_text

        try:
            mail.send(msg)
        except Exception as e:
            print(str(e))
        flash('Заказ оформлен!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@app.route('/calculator', methods=['GET'])
async def calculator():
    return render_template('calculator.html', form=ContactForm())
if __name__ == '__main__':
    app.run(debug=True)

