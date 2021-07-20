import pandas as pd
import smtplib

SenderAddress = "g1ur1vsinha@gmail.com"
password = "wubibhahpwdvlqum"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = """
    <p style="word-wrap:normal;">
    Hello this is a email form python khjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjsdlfkjjjjjjjjjjjjjj fjlaksdddddddddddddddddjsl jlkdf
    </p>
    """
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
# for email in emails:
server.sendmail(SenderAddress, ["golubspr@gmail.com"], body)
server.quit()