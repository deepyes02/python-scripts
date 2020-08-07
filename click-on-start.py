import pyautogui
#take a screenshot of the object you want to click

start_location = pyautogui.locateOnScreen('start.png')
print(start_location)

#Box(left:8, top=5, width=47, height=36)
left,top,width,height = start_location

#Point(x=31, y=23)
center = pyautogui.center((start_location))
print(center)

#move the mouse to the location
pyautogui.moveTo(center, duration=2)
#click
click = pyautogui.click(center)

