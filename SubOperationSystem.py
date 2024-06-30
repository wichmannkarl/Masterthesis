# +
# Import time
import time

# check if file exist
def checkIfFileExists(FilenameWithPath,ShowErrorMessage):
    # try to open file
    try:
        my_file = open(FilenameWithPath)
        my_file.close()
        return True
    except FileNotFoundError:
        if ShowErrorMessage:
            print("File:" + str(FilenameWithPath) + " does not exists. Exiting ...")
        return False

# ##########################################################################################################
    
# Timefunction
# ------------

# Get current time
def getTime():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

# Set time
def setTime():
    timeStart = time.time()
    return timeStart
    
# Get runtime
def getRuntime(timeStart):
    timeEnd = time.time()
    timeElapsed = timeEnd - timeStart
    return timeElapsed
