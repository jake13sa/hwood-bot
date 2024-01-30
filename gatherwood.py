import pyautogui
import time

center = [960, 540]
wait = time.sleep(0.246)
iteration = 0

pyautogui.getWindowsWithTitle("Heartwood Online")[0].activate()  # Focus on target window
time.sleep(1)

def press(key: str, duration: float):
    pyautogui.keyDown(key)
    time.sleep(duration)
    pyautogui.keyUp(key)

def work_pine(loop: int):
    while loop > 0:
        press("1", 0.3) # HEAL
        # FIRST TREE
        press("S", 0.55)
        wait
        press("D", 0.3)
        wait
        pyautogui.click(x=400,y=350)
        time.sleep(8) # CUTTING TREES

        press("1", 0.3) # HEAL
        # SECOND TREESD
        press("D", 0.5)
        wait
        pyautogui.click()
        time.sleep(8) # CUTTING TREES

        press("1", 0.3) # HEAL
        # THIRD TREE
        press("S", 1.5)
        wait
        pyautogui.click()
        time.sleep(8) # CUTTING TREES

        press("1", 0.3) # HEAL
        # FOURTH TREE
        press("D", 1.5)
        wait
        pyautogui.click()
        time.sleep(6) # CUTTING TREES

        press("1", 0.3) # HEAL
        # FIFTH TREE
        press("W", 1)
        wait
        pyautogui.click()
        time.sleep(6) # CUTTING TREES

        press("1", 0.3) # HEAL
        # SIXTH TREE
        press("A",3)
        wait
        pyautogui.click()
        time.sleep(6) # CUTTING TREES

        press("1", 0.3) # HEAL
        # SEVENTH TREE
        press("S", 0.5)
        wait
        pyautogui.click()
        time.sleep(8) # CUTTING TREES

        press("1", 0.3) # HEAL
        # 8
        press("A", 1)
        wait
        press("W",0.5)
        pyautogui.click()
        time.sleep(8) # CUTTING TREES

        press("1", 0.3) # HEAL
        # 9
        press("D", 1)
        wait
        pyautogui.click()
        time.sleep(8) # CUTTING TREES

        # BACK TO LOOP
        press("W", 2.5)
        wait
        press("D", 0.5)
        wait

        loop -= 1

def work_birch(loop: int):
    while loop > 0:
        # press("1", 0.3)
        # press("D", 0.55)    #1
        # wait
        # pyautogui.click(x=400,y=350)
        # time.sleep(8) # CUTTING TREES
        # press("S", 0.55)    #2
        # wait
        # pyautogui.click(x=400,y=350)
        # time.sleep(8) # CUTTING TREES
        # #press("1", 0.3)

        # press("A", 1)    #3
        # wait
        # pyautogui.click(x=400,y=350)
        # time.sleep(8) # CUTTING TREES
        # press("1", 0.3)

        # pyautogui.keyDown("D") #4
        # press("S", 1.5)
        # pyautogui.keyUp("D")
        # press("D", 1)
        # wait
        # pyautogui.click(x=400,y=350)
        # time.sleep(8) # CUTTING TREES
        # press("1", 0.3)

        # # pyautogui.keyDown("A") #5
        # # press("S", 0.7)
        # # pyautogui.keyUp("A")
        # # press("S", 1)
        press("A", 1)
        press("S", 0.7)
        wait
        pyautogui.click(x=400,y=350)
        # time.sleep(8) # CUTTING TREES
        # press("1", 0.3)

        press("W", 0.05)    #6
        press("D", 1.4)
        press("W", 0.2)
        exit()
        wait
        pyautogui.click(x=400,y=350)
        #time.sleep(8) # CUTTING TREES
        press("1", 0.3)

        press("S", 1)     #7
        press("A", 1.3) 
        press("w", 0.5)
        wait
        pyautogui.click(x=400,y=350)
        time.sleep(12) # CUTTING TREES

        press("S", 0.5) # GOING BACK TO POSITION
        press("A", 0.8)
        press("W", 2.3)

        loop -= 1
        print("LOOP: ",loop)

work_birch(10)