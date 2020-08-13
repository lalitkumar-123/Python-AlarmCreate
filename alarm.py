import time
import winsound
from win10toast import ToastNotifier

def timer(reminder,minutes):
    notificatior = ToastNotifier()

    notificatior.show_toast("Reminder",f"""Alarm will go off in (minutes) Min.""",duration=50)

    time.sleep(minutes * 60)

    notificatior.show_toast(f"Reminder",reminder,duration=50)

    #Alarm
    frequency = 2500 # 2500 hz
    duration = 1000 # 1 sec
    winsound.Beep(frequency,duration)

if __name__=="__main__":
    words = input("What would you remindes of: ")
    mins = int(input("Enter minutes: "))
    timer(words,mins)

