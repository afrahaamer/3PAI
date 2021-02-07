import time
import datetime
print("Current Time: ", datetime.datetime.now())
print("Current Year: ", datetime.date.today().strftime("%Y"))
print("Current Month: ", datetime.date.today().strftime("%B"))
print("Current Week: ", datetime.date.today().strftime("%W"))
print("Current Weekend: ", datetime.date.today().strftime("%w"))
print("Current Day of the Month: ", datetime.date.today().strftime("%j"))
print("Current Day of the Week: ", datetime.date.today().strftime("%A"))