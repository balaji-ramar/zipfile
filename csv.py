name="zipfile"
f=open("samples.zip")
print(name)
import os
f=open("samples.zip")
print(os.getcwd())
import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("samples.zip")))
print("Created: %s" % time.ctime(os.path.getctime("samples.zip")))



# from datetime import datetime
# filename = datetime.now().strftime('%d-%m-%y-%I-%M%p')
# print(filename)
