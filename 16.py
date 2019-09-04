class Time(object):
    """ Class that represents the time of day.     
        attributes: hour, minute, second """

    def __init__(self,hour=0,minute=0,second=0):
        seconds = hour*3600 + minute*60 + second
        self.hour = seconds/3600
        self.minute = (seconds%3600)/60
        self.second = (seconds%3600)%60

    def __int__(self):
        " edited version of Author "
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    def __str__(self):
        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)

    def __repr__(self):
        return '%.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)

    def __add__(self,other):
        seconds = int(self) + int(other)
        return Time(second=seconds)

    def __radd__(self,other):
        return self.__add__(other)

    def __mul__(self,mul):
        return Time(second= int(self) * mul)

    def __rmul__(self, mul):
        return self.__mul__(mul)

    def __cmp__(self,other):
        return cmp(int(self),int(other))

    def attributes(self):
        for attr, val in self.__dict__.items():
            print attr, val

    def increment(self, seconds):
        seconds += int(self)
        new=Time(second=seconds)
        self.hour=new.hour
        self.minute=new.minute
        self.second=new.second

    def greater(self, seconds):
        " edited version of Author "
        seconds += int(self)
        return Time(second=seconds)

    def speed(self,distance):
        " edited version of Author "
        return self*(1/distance)
    
    def is_after(self,other):
        return int(self) > int(other)

    def valid_time(time):
        " Author "
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return False
        return True

    def add_time(t1, t2):
        " Author "
        if not valid_time(t1) or not valid_time(t2):
            raise ValueError, 'invalid Time object in add_time'
        seconds = t1.time_to_int()+ t2.time_to_int()
        return int_to_time(seconds)




from datetime import date,datetime


def day_of_week():
    
    day={0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
    
    print 'The current weekday is %s.' % (day[date.weekday(date.today())])


def dates(year,month,day,hour,minute,second):
    
    dob=datetime(year,month,day,hour,minute,second)
    
    today=datetime.today()
    
    birthday=dob.replace(year = today.year)
    
    passed_already=birthday < today

    if passed_already: age = today.year - dob.year; time_until_next = birthday(year = birthday.year + 1) - today

    if not passed_already: age = today.year - dob.year - 1; time_until_next = birthday - today
    
    return {'age':age,'time_until_next':time_until_next}


def age(year,month,day,hour=0,minute=0,second=0):

    age=dates(year,month,day,hour,minute,second)['age']
    
    print 'Your current age is %d.' %(age)


def birthday_countdown(year,month,day,hour=0,minute=0,second=0):
    
    time_until_next=dates(year,month,day,hour,minute,second)['time_until_next']
    
    print 'You have %d day(s), %d hour(s), %d minute(s), and %d second(s) until your next birthday.' %(time_until_next.days,time_until_next.seconds/3600,time_until_next.seconds%3600/60,time_until_next.seconds%3600%60)
    

def double_day(b1, b2):
    """ Author

    Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    double_day = b1 + delta
    return double_day

def anyday(n,year1,month1,day1,year2,month2,day2):

    dob1=date(year1,month1,day1)
    dob2=date(year2,month2,day2)

    assert dob2 > dob1, 'DOB of person 2 is before that of person 1'
    assert n > 1, 'n is not greater than 1'

    delta = (dob2 - dob1) / (n - 1)

    return dob2 + delta
    

    
    
    


if __name__ == '__main__':

    time=Time()
    time.hour=11
    time.minute=59
    time.second=30
    print time
    time.attributes()


    time2=Time()
    time2.hour=12
    time2.minute=29
    time2.second=45
    print time2

    print time+time2
    print 'time cmp time2', time > time2
    
    print time.greater(3349)
    print Time(second=76854)

    print

    day_of_week()
    age(1998,8,26)
    birthday_countdown(1998,8,26)

    dylan=date(1998,8,26)
    cassie=date(2000,3,31)
    print double_day(cassie,dylan)
    print anyday(2,1998,8,26,2000,3,31)

    

