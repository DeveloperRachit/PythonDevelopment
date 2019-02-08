import psutil

print (psutil.cpu_times(percpu=False))
t=psutil.cpu_percent(interval=1)#blocking 
print (t)
#non blocking
t=psutil.cpu_percent(interval=None)#blocking 
print (t)
#blocking per-cpu
t=psutil.cpu_percent(interval=1,percpu=True)#blocking 
print (t)
cpu_count=psutil.cpu_count(logical=False)
print (cpu_count)
print (len(psutil.Process().cpu_affinity()))

#cpu_stats()


print("cpu Stats::",psutil.cpu_stats())
print("cpu Freq::",psutil.cpu_freq())
print("cpu Var mem::",psutil.virtual_memory())


print (psutil.net_io_counters(pernic=False, nowrap=True))
#running process

pr=psutil.pids()
print (pr)
print (psutil.process_iter())

for proc in  psutil.process_iter(attrs=['name','pid']):

    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

    except psutil.NoSuchProcess:
        pass 
    else:
        # print(proc.name())
        if proc.info['name']=='chrome.exe':
            print (proc.info['name'])
            print (proc.info['pid'])    
        # print (pinfo)
