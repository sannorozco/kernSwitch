from pyjoycon import ButtonEventJoyCon, get_R_id
import pygame
import pyautogui

joycon_id = get_R_id()
joycon = ButtonEventJoyCon(*joycon_id)

def getJoyStick():
	
	command = ""
	
	print("Horizontal: " + str( joycon.get_stick_right_horizontal() ))
	print("Vertical:   " + str( joycon.get_stick_right_vertical() ))
	
	if joycon.get_stick_right_horizontal() < 1000 and 1500 <= joycon.get_stick_right_vertical() <= 2500:
		command = "up"
	elif joycon.get_stick_right_horizontal() > 3000 and 1500 <= joycon.get_stick_right_vertical() <= 2500:
		command = "down"
	elif joycon.get_stick_right_vertical() < 1000 and joycon.get_stick_right_horizontal() > 1500:
		command = "left"
	elif joycon.get_stick_right_vertical() > 2500 and joycon.get_stick_right_horizontal() > 1500:
		command = "right"
	
	return command

while 1:
    pygame.time.wait(int(1000/60))

    for event_type, status in joycon.events():
        #print(joycon.get_status())
        #print(event_type)
        #print(status)
        #print(joycon.events())
        
        if event_type == "b" and status == 1:
            
            command = getJoyStick()
            print ("b: kern 1 " + command)
            pyautogui.keyDown('option')
            pyautogui.press(command)
            pyautogui.keyUp('option')
            
        elif event_type == "a" and status == 1:
            
            command = getJoyStick()
            print ("a: kern 5 " + command)
            pyautogui.keyDown('shift')
            pyautogui.press(command)
            pyautogui.keyUp('shift')
            
        elif event_type == "x" and status == 1:
            
            command = getJoyStick()
            print ("x: kern 10 " + command)
            pyautogui.keyDown('command')
            pyautogui.press(command)
            pyautogui.keyUp('command')

        elif event_type == "y" and status == 1:
            
            command = getJoyStick()
            print ("move: " + command)
            pyautogui.press(command)
        
        elif event_type == "right_sl" and status == 1:
            
            pyautogui.press('esc')
            
        elif event_type == "right_sr" and status == 1:
            
            pyautogui.press('enter')
        
        elif event_type == "r" and status == 1:
            
            pyautogui.keyDown('command')
            pyautogui.press("e")
            pyautogui.keyUp('command')
        
        elif event_type == "zr" and status == 1:
            
            pyautogui.keyDown('command')
            pyautogui.keyDown('option')
            pyautogui.press("e")
            pyautogui.keyDown('option')
            pyautogui.keyUp('command')
            
        elif event_type == "home" and status == 1:
            
            print ("exit ")
            exit()
            
