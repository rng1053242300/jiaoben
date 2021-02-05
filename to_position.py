import pyautogui
from PIL import Image
from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing
import os
import random
import time
import operator
import json


opera = {"+": operator.add, "-": operator.sub}  # etc.
fh = ["+", "-"]
ops = {"1": "jiesuan.png", "2": "jiesuanqian.png", "3": "tiaozhanhuangse.png"}


def to_position(file_name2):
    # pyautogui找图速率做对比
    res = pyautogui.locateCenterOnScreen(file_name2)
    return res


def random_click(x, y, r):
    suiji1 = random.randint(0, r)
    clickr = random.randint(1, 3)
    x1 = opera[random.choice(fh)](x, suiji1)
    y1 = opera[random.choice(fh)](y, suiji1)
    inva = random.uniform(a=0, b=1)
    pyautogui.click(x=x1, y=y1, clicks=clickr, interval=inva, button='left', duration=0.0, tween=pyautogui.linear)


# 子进程要执行的代码-挑战
def run_proc_tiaozhan():
    while True:
        res = to_position(ops["3"])
        if None is not res:
            x, y = res
            random_click(x, y, 40)
            time.sleep(19)
            print("点击挑战" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


# 子进程要执行的代码-结算前-太鼓
def run_proc_jiesuanqian():
    with open('./config.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        jiesuanqian = json_data['jiesuanqian']
    while True:
        if None is not to_position(ops["2"]):
            s = random.choice(jiesuanqian)
            x = s['x']
            y = s['y']
            r = s['r']
            random_click(x, y, r)
            print("点击结算前-太鼓" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


# 子进程要执行的代码-结算-达摩
def run_proc_jiesuan():
    with open('./config.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
        jiesuan = json_data['jiesuan']
    while True:
        if None is not to_position(ops["1"]):
            s = random.choice(jiesuan)
            x = s['x']
            y = s['y']
            r = s['r']
            random_click(x, y, r)
            print("点击结算-达摩" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print("*****************start")
    p = Pool(4)
    print("开启进程 挑战识别")
    p.apply_async(run_proc_tiaozhan, args=())
    print("开启进程 结算前-太鼓识别")
    p.apply_async(run_proc_jiesuanqian, args=())
    print("开启进程 结算-达摩识别")
    p.apply_async(run_proc_jiesuan, args=())
    p.close()
    p.join()
    print("结束进程 挑战")
    print("结束进程 结算前-太鼓识别")
    print("结束进程 结算-达摩识别")
    print("*****************end")



