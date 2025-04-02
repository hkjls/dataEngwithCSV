from datetime import datetime

def strtotime(strtime):
    time = datetime.strptime(strtime, "%H:%M:%S").time()
    hours = time.hour / 24
    minutes = ( time.minute / 60 ) / 24
    seconds = (( time.second /60) / 60 ) / 24
    
    int_time = hours + minutes + seconds
    return int_time