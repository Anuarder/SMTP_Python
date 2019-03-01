import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("saiko.mailserver@gmail.com", "Node122410")
server.sendmail(
    "saiko.mailserver@gmail.com",
    "anuar.ibraev97@gmail.com",
    "This message is from python"
)
server.quit()