# SendMail
Python script to send emails using local SMTP server.

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

## About DMARC

If a domain has a weak DMARC policy defined (*none*), you may spoof email addresses and send them to any address:
```
#Check DMARC policy and notice that it is set to none
> dig _dmarc.<domain.com> txt +short
"v=DMARC1; p=none;"
```

In this example, the DMARC policy exists, but is set to *none*. 
So a service (Outlook, Gmail, ...) receiving an email from `<domain.com>` will check what to do with unauthenticated/spoofed emails.
As the DMARC policy of the domain tells *none* ("do nothing"), the email will be sent to the recipient.

However, some services block spoofed emails by default. 
So depending on the recipient email service, the spoofed email may be blocked or be delivered with a warning.

For example, Outlook blocks spoofed emails, but Proton does not.
