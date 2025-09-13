import time
hour = int(time.strftime('%H'))  
print(hour)

if hour <= 12:
    print("Good Morning")
elif hour <= 18:
    print("Good Afternoon")
    

 
