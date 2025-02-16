import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(toEmail):
    # Email setup
    fromEmail = "barri.karthik11@gmail.com"  # Sender's email address
    appPassword = "jrkn mdge nhmw vyom"  # Email account password (use app-specific password for Gmail if needed)
    smtpServer = "smtp.gmail.com"  # SMTP server address
    smtpPort = 587  # SMTP port (587 for TLS, 465 for SSL)

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = "Test Email from Python"

    # Add the body of the email
    body = "This is a test email sent from Python!"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish connection to the SMTP server
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.starttls()  # Secure connection with TLS

        # Log in to the email server
        server.login(fromEmail, appPassword)

        # Send the email
        text = msg.as_string()
        server.sendmail(fromEmail, toEmail, text)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

# Call the function to send the email
toEmail = input("Enter Recepient Address: ")
send_email(toEmail)
