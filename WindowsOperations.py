import os
import datetime
import time


class WindowsOperations(object):
    def __init__(self, select_operation):
        self.select_operation=select_operation
    def all_operations(self):
        if self.select_operation=='shutdown':
            time.sleep(remaining_time)
            while True:
                if time_hour == datetime.datetime.now().hour and time_minutes == datetime.datetime.now().minute:  #
                    os.system("shutdown /s /t 1")
                    break
        if self.select_operation=='restart':
            time.sleep(remaining_time)
            while True:
                if time_hour == datetime.datetime.now().hour and time_minutes == datetime.datetime.now().minute:
                    os.system("shutdown /r /t 1")
                    break
        if self.select_operation=='open_app':
            app_name_open = input("Enter the application name you want to open: ").lower() + ".exe"
            time.sleep(remaining_time)
            while True:
                if time_hour == datetime.datetime.now().hour and time_minutes == datetime.datetime.now().minute:
                    os.startfile(app_name_open)
                    break
        if self.select_operation=='close_app':
            app_name_close = input("Enter the application name you want to close: ").lower() + ".exe"
            time.sleep(remaining_time)
            while True:
                if time_hour == datetime.datetime.now().hour and time_minutes == datetime.datetime.now().minute:
                    os.system("TASKKILL /F /IM " + app_name_close)
                    break




choice = int(input("Enter your choice \n1.Shutdown Windows \n2.Restart Windows "
                   "\n3.Open an application \n4.Close an application \n:"))
time_hour = int(input("Enter hour: "))
time_minutes = int(input("Enter minutes: "))
time_now = datetime.datetime.now()
remaining_time = ((time_minutes - time_now.minute) * 60 + (time_hour - time_now.hour) * 3600) % 86400
print(remaining_time)
if choice == 1:
   WindowsOperations('shutdown').all_operations()
elif choice == 2:
    WindowsOperations('restart').all_operations()
elif choice == 3:
    WindowsOperations('open_app').all_operations()
elif choice == 4:
    WindowsOperations('close_app').all_operations()
else:
    print("Please enter a valid input")
