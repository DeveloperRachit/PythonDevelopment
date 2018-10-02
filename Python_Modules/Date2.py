import time;  
  
localtime = time.asctime( time.localtime(time.time()) )  
print ("Formatted time :", localtime)  

print (time.time()  )

t = time.localtime()  
print (time.asctime(t))  