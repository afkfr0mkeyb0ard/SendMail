from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
import sys

msg = EmailMessage()

if "-h" in sys.argv:
	print("""> python3 sendmail.py -to "recipient@domain.com" -from "sender@domain.com" -t "newoffer.html" -s 'New offer for you' [-H] [-rt 'attacker@domain.com'] """)
	print("	-to 	recipient email address")
	print("	-from 	sender email address")
	print("	-t 	email template (HTML file in /templates folder)")
	print("	-s 	email subject")
	print("	-H 	set High priority email (optional)")
	print("	-rt	set reply-to header to automatically reply to another address (optional)")
	sys.exit()

if not "-to" in sys.argv:
	sys.exit("[-] Please specify an address where to send the mail (-to recipient@domain.com).")
else:
	i = sys.argv.index("-to")
	try:
		EMAIL_TO = sys.argv[i+1]
	except:
		sys.exit("[-] The recipient address is invalid (-to recipient@domain.com).")
		
	
if not "-from" in sys.argv:
	sys.exit("[-] Please specify a sender address (-from sender@domain.com).")
else:
	i = sys.argv.index("-from")
	try:
		EMAIL_FROM = sys.argv[i+1]
	except:
		sys.exit("[-] The sender address is invalid (-from sender@domain.com).")

if not "-t" in sys.argv:
	sys.exit("[-] Please specify a template file (-t newoffer.html).")
else:
	i = sys.argv.index("-t")
	try:
		TEMPLATE = sys.argv[i+1]
	except Exception as e:
		sys.exit("[-] The template file is invalid or does not exist (-t newoffer.html).")

if not "-s" in sys.argv:
	sys.exit("[-] Please specify a subject (-s 'New offer!!').")
else:
	i = sys.argv.index("-s")
	try:
		SUBJECT = sys.argv[i+1]
	except Exception as e:
		sys.exit("[-] The subject is invalid (-s 'New offer!!').")

if "-rt" in sys.argv:
	i = sys.argv.index("-rt")
	try:
		REPLY_TO = sys.argv[i+1]
	except Exception as e:
		sys.exit("[-] The reply-to address is invalid (-rt attacker@domain.com).")


with open('templates/'+TEMPLATE, 'r') as f:
    email_body = f.read()

msg = MIMEText(email_body,'html')
msg["Subject"] = SUBJECT
print("[+] Subject: " + SUBJECT)
if "-H" in sys.argv:
	msg['X-MSMail-Priority'] = 'High'
	print("[+] Set email priority to High")
msg["From"] = EMAIL_FROM
print("[+] Sender: " + EMAIL_FROM)
msg["To"] = EMAIL_TO
print("[+] Sending to: " + EMAIL_TO)
if "-rt" in sys.argv:
	msg.add_header("reply-to",REPLY_TO)
	print("[+] Set reply-to: " + REPLY_TO)
s = smtplib.SMTP("localhost")
s.send_message(msg)
print("[+] Email sent successfully!")
