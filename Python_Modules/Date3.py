import time  
import calendar  
localtime = time.asctime( time.localtime(time.time()) )  
print (localtime)  
time.sleep( 10 )  
localtime = time.asctime( time.localtime(time.time()) )  
print (localtime)  

  
timerequired = time.strptime("26 Jun 14", "%d %b %y")  
print (timerequired)
t = (2014, 6, 26, 17, 3, 38, 1, 48, 0)  
t = time.mktime(t)  
print (time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))    




print ("Current month is:")  
cal = calendar.month(2018, 10)  
print (cal)  