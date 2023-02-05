import imaplib

host = 'mail.privateemail.com'
user = 'stewmartbills@petestewart.dev'
password = 'StewMart#911'


def get_emails():
    emails = []
    # Connect securely with SSL
    imap = imaplib.IMAP4_SSL(host)

    # Login to remote server
    imap.login(user, password)

    imap.select('Inbox')
    tmp, messages = imap.search(None, '(UNSEEN)')
    for num in messages[0].split():
        # Retrieve email message by ID
        tmp, data = imap.fetch(num, '(RFC822)')
        emails.append({'id': num.decode("utf-8"), 'message': data[0][1].decode("utf-8")})
    imap.close()
    imap.logout()
    return emails


def mark_read(email_id):
    imap = imaplib.IMAP4_SSL(host)
    imap.login(user, password)
    imap.select('Inbox', readonly=False)
    imap.store(email_id, '+FLAGS', '\Seen')
    imap.close()
    imap.logout()
    return
