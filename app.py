
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
CORS(app, support_credentials=True)

gmail = {
    'user': '',
    'password': ''
}

@app.route('/')
def main():
    return "<h1>All Work</h1>"


@app.route('/sendMail', methods=['POST'])
@cross_origin(supports_credentials=True)
def sendMail():
    data = request.get_json()  # Запись данных из POST запроса
    try:
        smtpServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpServer.login(gmail["user"], gmail["password"])

        message = MIMEMultipart()
        message["Subject"] = data["subject"]
        message["To"] = data["email"]
        message["From"] = gmail["email"]
        html = """\
        <html>
        <body>
            <p>
                <div>Имя: {name}</div>
                <div>Телефон: <a href="tel:{phone}">{phone}</a></div>
            </p>
        </body>
        </html>
        """.format(name=data["name"], phone=data["phone"], message=data["message"])

        part1 = MIMEText(html, 'html')
        message.attach(part1)

        smtpServer.sendmail(
            gmail["email"],
            data["email"],
            message.as_string()
        )

        smtpServer.quit()

        return jsonify({"message": "Successfully sent email"})

    except Exception as err:
        print("Error to send email: %s" % err)
        return jsonify({"error": err})


if __name__ == '__main__':
    app.run()
