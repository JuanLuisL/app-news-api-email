import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "oreillytest23@gmail.com"
    password = "gkhcrckjtyklcipg"

    receiver = "oreillytest23@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, timeout=120) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
