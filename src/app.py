from flask import Flask, jsonify, request
from flask_cors import CORS

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


app = Flask(__name__)
CORS(app)


gmail = {
    'user': 'saiko.mailserver@gmail.com',
    'password': 'Node122410'
}


@app.route('/')
def send():
    return jsonify({'message': "All ok"})


@app.route('/sendMail', methods=['POST'])
def sendMail():
    data = request.get_json()  # Запись данных из POST запроса
    try:
        message = MIMEMultipart()
        message["Subject"] = data["Subject"]
        message["To"] = data["email"]
        message["From"] = "saiko.mailserver@gmail.com"
        text_message = MIMEText(data["message"], "plain")
        message.attach(text_message)

        smtpServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpServer.login(gmail["user"], gmail["password"])
        smtpServer.sendmail(
            "saiko.mailserver@gmail.com",
            data["email"],
            message.as_string()
        )

        smtpServer.quit()

        return jsonify({"message": "Successfully sent email"})

    except Exception as err:
        print("Error to send email: %s" % err)
        return jsonify({"error": err})


if __name__ == '__main__':
    app.run(debug=True)
