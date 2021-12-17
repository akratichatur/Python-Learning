import psutil
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
plugged = "Plugged In" if plugged else "Not Plugged In"
print(percent+'% | '+plugged)



'''https://stackoverflow.com/questions/15015026/create-python-script-that-runs-at-startup

https://www.geeksforgeeks.org/convert-python-script-to-exe-file/

'''