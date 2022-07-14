#sk/\

# import excel_reader1 
# import share_data_over_mail
import smtplib
import pandas as pd 


#reading and sorting the data

file_location = "marks_sheet.csv"
excel_data = excel_reader1.extract_data_with_marks_greater_than_500(file_location)
# print(excel_data)
# success, message = share_data_over_mail.send_data_over_mail(excel_data)
# print("Mail Sent - ", success)
# print('Message - ', message)

## Parsing and extracting the data


   

def extract_data_with_marks_greater_than_500(file_location):
        
    # Read the file    
    data = pd.read_csv(file_location, low_memory=False)
    # Output the number of rows    
    # print("Total rows: {0}".format(len(data)))   
    greater_than_500 = data[data['Marks'] > 500 ]
    return greater_than_500


## sharing data over mail.

gmail_user = 'ajjaloky@gmail.com'
gmail_password = 'pnupsaqtkvhutnsi'

sent_from = gmail_user
to = ['salokesh99@gmail.com','lokesh.k4@delhivery.com']
subject = 'sample Subject'
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
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

