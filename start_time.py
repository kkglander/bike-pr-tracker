import time, traceback, sys
import logger, context

with open(context.path + ".Init_Time.csv", "r") as f:
    saved = f.readline()

Tformated = time.strftime("%H.%M.%S")
Dformated = time.strftime("%d.%m.%Y")
try:
    with open(context.path + ".Init_Time.csv", "w") as f:
        f.write(f"{Tformated}, {Dformated}")
    logger.log("start time successfully saved")

except Exception as error:
    exc_type, exc_obj, exc_tb = sys.exc_info()  #-|
    tb_list = traceback.extract_tb(exc_tb)      # |- This is AI code, should look into deeper bc it looks interesting
    line_number = tb_list[-1].lineno            #-|
    logger.logError(f"{error} on line {line_number}")
    with open(context.path + ".Init_Time.csv", "w") as f:
        f.write(saved)
