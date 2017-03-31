# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile='/path/to/textfile'
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
me='foo@mail1.com'
you='bar@mail2.com'
msg['Subject'] = 'The contents of %s' % textfile
msg['Froim'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
#s = smtplib.SMTP('localhost')
s = smtplib.SMTP(host='smtp.website.com', port=587)
s.starttls()
s.login('foo','bar')
s.sendmail(me, [you], msg.as_string())
s.quit()
