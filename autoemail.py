import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

gmail_user = 'guruprasadnayak24@gmail.com'
gmail_password = 'Sample Password'

sent_from = 'gp007ification24@gmail.com'
subject = '1st Transport Battalion - 46th Anniversary'
body = "!\nWelcome to the 1st Transport Battalion's 46th Anniversary event. This is an auto-generated email. You are now registered for the event, as well as the luckydraw!\n"

def sendMail(recepient, name, lnum):
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = recepient
    msg['Subject'] = subject
    mail = ("Good Evening " + name + body + 
            "\nYour name is registered as " + name + "; and your draw number is: " + str(lnum) + 
            ". Look forward to our Lucky Draw, you may be called up on stage to recieve a prize!" +
            "\n\nThank you for joining us this evening! Wishing you the best of luck and a great evening ahead!\n" + 
            "\nBest regards,\nSCT Guru")
    msg.attach(MIMEText(mail, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, recepient, msg.as_string())
        # print(name,'\'s Email sent successfully!')
    except Exception as e:
        print('Failed to send email. Error:', str(e))
    finally:
        server.quit()

def sendWinMail(recepient, nric, name, prize):
    winbody = ("Hello again " + name + 
               ",\n\nThe last 4 digits of your NRIC are " + nric +
              ".\n\nCongratulations on winning the " +prize+"! Please come to the stage to collect your prize!\n\n"+
              "Please bring identification that contains your NRIC number to verify your identity." + 
              "\n\nBest regards,\nSCT Guru")
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = recepient
    msg['Subject'] = "Congratulations! You have won the " + prize
    msg.attach(MIMEText(winbody, 'plain'))

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, recepient, msg.as_string())
        print(name,'\'s Email sent successfully!')
    except Exception as e:
        print('Failed to send email. Error:', str(e))
    finally:
        server.quit()

# sendMail("gp007ification@gmail.com", 'Guru', 1110)

def send_bulk_mail(mail_list):
    sent = 0
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        for i in mail_list:
            try: 
                sendMail1(i[3], i[1], 1233 + sent, server)
                sent += 1
                print("Mails sent = ", sent)
            except:
                print("Didnt send email to " + i[1])
    finally:
        server.quit()
    return sent

def sendMail1(recepient, name, lnum, server):
    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = recepient
    msg['Subject'] = subject
    mail = ("Good Evening " + name + body + 
            "\nYour name is registered as " + name + "; and your draw number is: " + str(lnum) + 
            ". Look forward to our Lucky Draw, you may be called up on stage to recieve a prize!" +
            "\n\nThank you for joining us this evening! Wishing you the best of luck and a great evening ahead!\n" + 
            "\nBest regards,\nSCT Guru")
    msg.attach(MIMEText(mail, 'plain'))

    try:
        server.sendmail(sent_from, recepient, msg.as_string())
    except Exception as e:
        print('Failed to send email. Error:', str(e))