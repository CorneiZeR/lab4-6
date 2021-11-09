from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecret'
app.config['SECURITY_PASSWORD_SALT'] = 'thisisasecretsalt'


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nopalko19@gmail.com'
app.config['MAIL_PASSWORD'] = 'okjcqaobidwqhflw'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=["GET","POST"])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        msg = Message(subject = f'Питання з Shockspeare від {request.form["name"]}', 
            sender = request.form['email'], 
            recipients = ['nopalko19@gmail.com'], 
            body = request.form['message'] + '\n\n\nЛист отримано з сайту Shockspeare')

        mail.send(msg)
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)


@app.route('/schedule')
def schedule():
    return render_template('schedule.html')


if __name__ == '__main__':
    app.run(debug=True)