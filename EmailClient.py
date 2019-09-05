# A simple one-time Email client(only be used to send one email at a time) with python
import smtplib #using smtplib to do the job

conn = smtplib.SMTP("smtp.gmail.com",587) #making an smtp connection

conn.ehlo() #connecting to the email 

ret = conn.starttls() #encrypting the connection

if(ret[0] != 220): #to check if there is an error with our encryption
    print("Error with encryption")
    exit(0)

email = input("Enter your email:") #taking the email
pas = input("Enter the password:") #taking the password (if that doesn't connect use Google app password)

conn.login(email,pas) #logging in 

rcemail = input("Enter the recipient's E-mail:") #taking the the receiver's email 

sub = "Subject:" + input("Enter the subject:") #adding the subject
sub += '\n\n'

message = str()

print("Enter your message(Enter 0 after Enter to finish the message):")

while(True):
    #taking in message until user hits 0
    tempmes = input()
    if(tempmes == '0'):
        break
    message += tempmes
    message += '\n'

messa = sub + message #making the message
conn.sendmail(email , rcemail,messa) #sending the email

print("\nMESSAGE SENT SUCCESSFULLY") # message sent successfully 