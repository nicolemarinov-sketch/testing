from threading import Thread
counter=0
counter_lock = Lock() # יצירת מנעול ושימוש במיוטקס
def increment_counter():
    for i in range (100000):
        with counter_lock:
            global counter += 1

def decrement_counter():
    for i in range (100000):
        with counter_lock:
            global counter -= 1

thread1 = Thread(target = increment_counter)
thread2 = Thread(target = decrement_counter)
thread1.start() # מאתחל את הטרד
thread2.start()

thread1.join()# מחכה במיין שכל הטרדים האחרים יסיימו לפני שממדיכים בקוד ומדפיסים את התוצאה
thread2.join()

print("the final counter  value is: ",counter)