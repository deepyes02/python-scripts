import pyautogui, time
#open a paint app, you have five seconds to adjust the mouse
#before this program starts her magic
def drawthis():
  draw = pyautogui
  time.sleep(5)
  #take your mouse to the program during the 5 seconds delay
  pyautogui.click()

  distance = 200
  while distance > 0:
    draw.dragRel(distance, 0, duration=0.2) #move right
    distance = distance - 5
    pyautogui.dragRel(0,distance,duration=0.2) #move down
    pyautogui.dragRel(-distance, 0, duration=0.2) #move left
    distance = distance -5
    pyautogui.dragRel(0, -distance, duration=0.2) #move up
    