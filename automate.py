import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

store width,height of screen as variables
width, height = pyautogui.size()

def squareMove():
  for i in range(3):
    pyautogui.moveTo(100,100, duration=0.25)
    pyautogui.moveTo(200,100, duration=0.25)
    pyautogui.moveTo(200,200, duration=0.25)
    pyautogui.moveTo(100,200, duration=0.25)

# squareMove()


def relativeMove():
  for i in range(2):
    pyautogui.moveRel(100,0,duration=0.25)
    pyautogui.moveRel(0,100,duration=0.25)
    pyautogui.moveRel(-100,0,duration=0.25)
    pyautogui.moveRel(0,-100,duration=0.25)


relativeMove()





