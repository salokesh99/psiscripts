import smtplib
import excel_reader1


# def send_data_over_mail(data):

gmail_user = 'ajjaloky@gmail.com'
gmail_password = 'pnupsaqtkvhutnsi'

sent_from = gmail_user
to = ['salokesh99@gmail.com', 'lokesh.k4@delhivery.com']
subject = 'students with Marks greater than 500'
# body = str(data)
body = "sample Body"


file_location = "marks_sheet.csv"
excel_data = excel_reader1.extract_data_with_marks_greater_than_500(file_location)
body = excel_data

email_text = """\
From: %s 
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print( True ,"Email sent successfully!" )
except Exception as ex:
    print( False, "Something went wrong….", ex  )

