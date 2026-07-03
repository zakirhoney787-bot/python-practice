import time as t
from plyer import notification

# Get the local time
current = t.localtime()
currenthour = current.tm_hour

# Display the current hour in the console
print("Current hour:", currenthour)

# Check the hour to print the correct greeting
if 18 < currenthour < 24:
    print("Good night")
else:
    print("Good morning")

# Optional: Send a desktop notification
notification.notify(
    title="Greeting",
    message="Hope you are having a great day!",
    timeout=5
)
