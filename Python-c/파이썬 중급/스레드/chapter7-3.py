from multiprocessing import Process
import time


class Subprocess(Process):

    def __init__(self, name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")


if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name="startcoding")
    p.start()
    time.sleep(2)
    #p.join()
    
#프로 세스가 살아 있는지 검사
    print(p.is_alive())
    print("[main] end")
