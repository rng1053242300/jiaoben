from multiprocessing import Process
import os
import to_position
import random
import time

def test_check():
    # pyautogui找图速率做对比
    a1, a2 = to_position.get_position("./quantu.png", "./tiaozhanhuangse.png")
    return a1, a2
    # print(a1, a2)


# 子进程要执行的代码
def run_proc(name, i):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    while i <= 1500:
        if None is not test_check():
            print("click第" + str(i) + "次")
            time.sleep(3)
            i = i + 1


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test', 1, ))
    print('Child process will start.')
    p.start()
    p.join()
    p.terminate()
    print('Child process end.')
