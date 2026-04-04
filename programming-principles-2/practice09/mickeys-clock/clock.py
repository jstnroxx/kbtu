from datetime import datetime

def getCurrentTime():
    timeNow = datetime.now().time()
    
    return {
        "minutes" : timeNow.minute,
        "seconds" : timeNow.second,
        "milliseconds" : timeNow.microsecond // 1000
    }