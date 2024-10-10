import datetime

date = datetime.date(2025,1,2)
today = datetime.date.today()
time = datetime.time(12,30,0)
now = datetime.datetime.now()

# to format the appearance
now2 = now.strftime("Time :: %H:%M:%S    Date :: %d-%m-%y")


print(today)
print(date)
print(time)
print(now)
print(now2)

target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date is in the past")
else:
    print("Target date is in the future")  
