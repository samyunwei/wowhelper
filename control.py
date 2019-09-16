import pyautogui
import random
import time

count = 0
direct_dict = {0: "w", 1: "s", 2: "q", 3: "e"}
wait_time = 15
pos_offset = 20 #根据自己的分辨率来设置


def RightMouseClicked(sleep_time):
    print("15s to begin:")
    pyautogui.sleep(15)
    x, y = pyautogui.position()
    print("mouse in x:%d y:%d", x, y)
    pyautogui.click(x, y, button="right")
    pyautogui.sleep(sleep_time)
    pyautogui.click(x - pos_offset, y, button="right")
    pyautogui.moveTo(x, y)


def forward_move(step):
    pyautogui.keyDown(direct_dict[step % 4])
    time.sleep(step)
    pyautogui.keyUp(direct_dict[step % 4])


while True:
    if count % 3 == 0:
        timeout = random.randint(10, 20)
        RightMouseClicked(timeout)
    else:
        step = random.randint(4, 10)
        pyautogui.typewrite("  ", 60)
    count += 1
