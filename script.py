import threading
import time

def walk_dog():
    time.sleep(3)
    print("Im walking the dog right now...")


def take_out_thrash():
    time.sleep(1)
    print("Im taking the thrash out right now...")


def get_mail():
    print("Im getting the mail right now...")


if __name__ == '__main__':
    print("========= NORMAL EXECUTION WITHOUT THREADS ==============")
    walk_dog()
    take_out_thrash()
    get_mail()
    print("DONE")



    print("========= SPECIAL EXECUTION WITH THREADS ==============")
    t1 = threading.Thread(target=walk_dog)
    t2 = threading.Thread(target=take_out_thrash)
    t3 = threading.Thread(target=get_mail)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    print("DONE")