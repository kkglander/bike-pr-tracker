#Quick functions that i whipped up so that i would have a log file to check for various reasons
import time, context

def appendLog(string):
    currTime = time.strftime("%d.%m.%Y|%H:%M:%S")
    string = f"{currTime} - {string}\n"
    with open(context.path + "log.txt","a") as log:
        log.write(string)


def logError(errorMsg):
    string = f"ERROR: {errorMsg}"
    appendLog(string)


def log(message):
    appendLog(message)


if __name__ == "__main__":
    print("Testing Log Function")
    log("TEST MESSAGE")
    logError("TEST ERROR")
