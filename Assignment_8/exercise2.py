import datetime

class Date:

    def __init__(self,time):
       self.time = time

    def add(self,time):
       fulldate = datetime.datetime(100, 1, 1, self.time.hour, self.time.minute, self.time.second)
       fulldate = fulldate + datetime.timedelta(seconds=time.time.second ,hours=time.time.hour , minutes=time.time.minute)
       return Date(fulldate)


    def sub(self,time):
       fulldate = datetime.datetime(100, 1, 1, self.time.hour, self.time.minute, self.time.second)
       fulldate = fulldate - datetime.timedelta(seconds=time.time.second ,hours=time.time.hour , minutes=time.time.minute)
       return Date(fulldate)

    def toDate(self):
        time = datetime.datetime.fromtimestamp(self.time.second)
        return time.strftime('%m/%d/%Y %H:%M:%S %Z')

    def getTimeStamp(self):
        return self.time


a = Date(datetime.datetime(100,1,1,11,34,59))
b = Date(datetime.datetime(100,1,1,4,34,9))



print(a.add(b))
