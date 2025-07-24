import sys
import logger, context
from datetime import datetime

#Getting the duration of the ride
try:
    currObj = datetime.now()
    currDate = currObj.strftime("%d.%m.%Y")
    format = "%H.%M.%S, %d.%m.%Y"

    with open(context.path + ".Init_Time.csv", "r") as f:
        t1RAW = (f.readline())
        t1 = datetime.strptime(t1RAW, format) #turns the saved time into a datetime object
        startDate = t1.strftime("%d.%m.%Y")

    if startDate != currDate:
        logger.logError(f"Cycle dates do not match: {startDate} and {currDate}")
        sys.exit("Cycle dates do not match")
    else:
        diff = currObj - t1
        total_sec = int(diff.total_seconds())

        hours = total_sec // 3600
        minutes = (total_sec % 3600) // 60
        seconds = total_sec % 60 

        timeTaken = f"{hours:02}.{minutes:02}.{seconds:02}"
        # print(timeTaken)
        logger.log("successfully calculated duration of workout")
        with open(context.path+".Init_Time.csv", "w") as f:
            f.write("")
            
except:
    logger.logError("failed to calculate duration of workout")
    sys.exit()

#Loggin the Duration
with open(context.path + "times.csv","a") as f:
    f.write(f"{currDate}\t{timeTaken}\n")

print("200")
