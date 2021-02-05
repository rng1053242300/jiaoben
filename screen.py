import pyautogui
import time


ops = {"1": "jiesuan.png", "2": "jiesuanqian.png", "3": "tiaozhanhuangse.png"}
print("选择文件名称 1-jiesuan.png 2-jiesuanqian.png 3-tiaozhanhuangse.png")
name = ops[input()]
print(name)
print("输入（左上定点）初始位置坐标x")
x = input()
print("输入（左上定点）初始位置坐标y")
y = input()
print("输入图块宽")
weight = input()
print("输入图块高")
height = input()
pic_3 = pyautogui.screenshot(name, region=(x, y, weight, height))
print("截图成功")
