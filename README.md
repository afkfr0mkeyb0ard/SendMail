# SendMail
Python script to send emails using local SMTP server

## Install dependencies

```
> sudo apt-get install sendmail
> sudo systemctl start sendmail.service
```

## How to use

```
> python3 sendmail.py -to 'recipient@domain.com' -from 'sender@domain.com' -t 'newoffer.html' -s 'New offer for you' [-H] [-rt 'attacker@domain.com']
	-to 	recipient email address
	-from 	sender email address
	-t 	email template (HTML file in /templates folder)
	-s 	email subject
	-H 	set High priority email (optional)
	-rt	set reply-to header to automatically reply to another address (optional)
```
