import pyautogui as pg #using pyautogui to 
import time

for i in range(60): #we send 60 messages

    #zoom your browrser to 150%
    box = pg.locateOnScreen('plus.png')
    print(box)
    print(box[0]) #box[0] is the left coordinate 
    
    #we actually find the location of PLUS icon in the discord chat
    #thenchange the LEFT coordinate to LEFT+190 so that we select the mesaage box to type the message
    yex = box[0]+180 
    
    #similarly we do the same here
    why = box[1]+25
    
    #simulate click
    pg.click(yex, why)
    
    #to enter the message in the text box
    pg.typewrite("message " + str(i + 1) + " Out of 60") #you can use any messages here
    
    #simulating enter to send the message
    pg.press('enter')
    print('done')
    
    #not to crash the script hence we give a second break
    time.sleep(1) 