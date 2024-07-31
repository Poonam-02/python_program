import time
current_time = time.strftime('%H:%M:%S')
print(current_time)
hour = int(time.strftime('%H'))

if 0 <= hour < 12:
    print("Good Morning!!!")
elif 12 <= hour < 16:
    print("Good Afternoon!!!")
elif 16 <= hour < 18:
    print("Good Evening!!!")
elif 18 <= hour <= 24:
    print("Good Night!!!")
