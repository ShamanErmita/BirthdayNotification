import time
import os
from plyer import notification

birthdayFile = '/path/to/birthday/file'

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    birthdays_today = []

    for line in fileName:
        if today in line:
            line = line.split(' ')
            full_name = line[1] + ' ' + line[2]
            birthdays_today.append(full_name)

    if birthdays_today:
        message = "".join(birthdays_today)
        notification.notify(
                title = "Aniversários Hoje: ",
                message =  message,
                timeout = 10
            )
    else:
        notification.notify(
            message = "Não Existem Aniversários Hoje ;(",
            timeout = 10
        )

if __name__ == '__main__':
    checkTodaysBirthdays()