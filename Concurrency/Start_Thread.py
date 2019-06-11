import threading
import time

def handler(started=0,finished=0):
    result=0
    for i in range (started,finished):
        result+=1
    print('Values',result)

params={'finished':2 **26}

task = threaing.Thread(target=handler, kwargs=params)
started_at=time.time()
print('RESULTS 1')
task.start()
task.join()
print('Time :{}'.format(time.time()-started_at))

started_at=time.time()
print('RESULTS 2')
handler(**params)
print('Time:{}'.format(time.time()-started_at))   