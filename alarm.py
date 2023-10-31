import time
from playsound import playsound

def set_custom_alarm_time():
    custom_hour = int(input("Enter the hour (in 24-hour format): "))
    custom_minutes = int(input("Enter the minute: "))
    return custom_hour, custom_minutes

def initiate_custom_alarm(custom_hour, custom_minutes):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == custom_hour and current_time.tm_min == custom_minutes:
            print("Time's up! Alarm ringing...")

            # Play the alarm sound
            playsound("C:\\Users\\nadigergagan\\Downloads\\Alarm-Fast-A1-www.fesliyanstudios.com.mp3") 

            # Ask if user wants to snooze or stop the alarm
            choice = input("Press 's' to snooze or any other key to stop: ")
            if choice.lower() == 's':
                custom_minutes += 5  # Snooze for 5 minutes
                if custom_minutes >= 60:
                    custom_hour = (custom_hour + 1) % 24
                    custom_minutes -= 60
            else:
                break

        time.sleep(60)

if __name__ == "__main__":
    print("SET YOUR CUSTOM ALARM TIME: ")
    alarm_hours, alarm_minutes = set_custom_alarm_time()
    initiate_custom_alarm(alarm_hours, alarm_minutes)
