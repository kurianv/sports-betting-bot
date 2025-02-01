import smtplib
import bets

stmp_server = smtplib.SMTP('smtp.gmail.com', 587)
stmp_server.ehlo()

stmp_server.starttls()
sender = 'sender@gmail.com'
receiver = ['reciever1@gmail.com', 'reciever2@gmail.com']
password = '#### #### #### ####' #hidden for security reasons
subject = 'IMPORTANT: Bets to Make for NFL'
text = bets.feasibleBets()
for i in range(len(receiver)):
  BODY = "\r\n".join((
              "From: %s" % sender,
              "To: %s" % receiver[i],
              "Subject: %s" % subject,
              "",
              text
              ))

  stmp_server.login(sender, password)
  stmp_server.sendmail(sender, receiver[i], BODY.encode('utf-8'))
print("Email Sent")


