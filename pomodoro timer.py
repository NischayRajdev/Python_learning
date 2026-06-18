import time

sessions = int(input("enter the number of sessions : "))

def work_time(mins):
    seconds = mins * 60
    print("Work Time On")
    while seconds > 0:
        hours = seconds // 3600
        mins_display = (seconds % 3600) // 60
        secs = seconds % 60
        print(f"\r{hours:02d}:{mins_display:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\r00:00:00")
    print("Time's Up!")


def break_time(mins):
    if mins <= 60:
        return 5
    elif mins <= 120:
        return 10
    else:
        return 15

def break_timecount(break_mins):
    break_seconds = break_mins* 60
    while break_seconds > 0 : 
    
     break_hours = break_seconds //3600
     break_mins = (break_seconds % 3600) // 60
     break_secs = break_seconds % 60
     print (f"\r{break_hours:02d}:{break_mins:02d}:{break_secs:02d}",end="")

     time.sleep(1)

     break_seconds -=1


    print("\r00.00.00")
    print("Break over!")

    
mins = int(input("enter the time in minutes: "))

for session in range(1, sessions + 1):
    print(f"\nSession {session}/{sessions}")
    work_time(mins)

    if session == sessions:
        print("All sessions completed!")
        break

    if session % 4 == 0:
        print("Long break")
        break_mins = 30
        break_timecount(break_mins)
    else:
        print("Short break")
        break_mins = break_time(mins)
        break_timecount(break_mins)

    print(f"Break time : {break_mins} minutes")

total_focustime = sessions * mins
print("pomodoro session done")

