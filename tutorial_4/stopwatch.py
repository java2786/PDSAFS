import time

# time -> decrease time -> when 0 -> stop 
timer = 299
while(timer>0):
    print(timer//60,":",timer%60)
    timer = timer - 1
    time.sleep(1)

print("TIME IS UP")
        