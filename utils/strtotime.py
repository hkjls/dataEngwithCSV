from datetime import datetime, time

class setTime:
    
    def __init__(self):
        pass

    def strtoday(self, strtime:str)-> float: #to convert time to day
        time = datetime.strptime(strtime, "%H:%M:%S").time()
        hours = time.hour
        minutes = ( time.minute / 60 )
        seconds = (( time.second /60) / 60 )
        
        int_time = hours + minutes + seconds
        
        return int_time/24
    
    def strtimetosecond(self, strtime:str)-> float:
        time = datetime.strptime(strtime, "%H:%M:%S").time()
        hours = time.hour * 3600
        minutes = time.minute * 60
        seconds = time.second
        
        int_time = hours + minutes + seconds
        
        return int_time
    
    def timetostr(self, floatTime:float)-> str:
        h, min =  divmod(floatTime, 1)
        min, s = divmod(min*60, 1)
        s = s*60
        strtime = "%02d:%02d:%02d" % (h, min, s)
        return strtime


if __name__ == "__main__":
    print(setTime().strtoday("23:00:00")) # str time to n day
    print(setTime().timetostr(2.52)) # hour (float) to time
    print(setTime().strtimetosecond("23:00:00")) # str time to seconde