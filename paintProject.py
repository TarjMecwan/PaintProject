from pygame import *
from math import *
from random import *
import pygame as pg
from tkinter import *
from tkinter import filedialog

root=Tk()
root.withdraw() #hides the extra window
init()
font.init()
comicFont=font.SysFont("Comic Sans MC", 23) #setting the font
loadButtonText="LOAD" #text for LOAD button
loadButtonPic=comicFont.render(loadButtonText,False,(255,255,255)) #rendering the LOAD button
saveButtonText="SAVE" #text for SAVE button
saveButtonPic=comicFont.render(saveButtonText,False,(255,255,255)) #rendering the SAVE button

width,height=1470,830 #width/height
screen=display.set_mode((width,height)) #setting display
RED=(255,0,0) #RED COLOR
GREY=(127,127,127) #GREY COLOR
BLACK=(0,0,0,200) #BLACK COLOR
BLUE=(0,0,255) #BLUE COLOR
GREEN=(0,255,0) #GREEN COLOR
YELLOW=(255,255,0) #YELLOW COLOR
WHITE=(255,255,255) #WHITE COLOR
shapeFill=False #fills shape

rad=0 #radius
pencilRect=Rect(170,30,35,35) #pencil
eraserRect=Rect(220,30,35,35) #eraser
highlighterRect=Rect(270,30,35,35) #highlighter
rectangleToolRect=Rect(389,30,35,35) #rectangle
ellipseToolRect=Rect(539,30,35,35) #ellipse
canvasRect=Rect(0,140,1470,534) #CANVAS
fountainPenRect=Rect(320,30,35,35) #fountain pen
lineToolRect=Rect(539,80,35,35) #line
sprayPaintToolRect=Rect(170,80,35,35) #spray paint
brushToolRect=Rect(270,80,35,35) #brush
colourPickerToolRect=Rect(220,80,35,35) #color picker
fillPaintToolRect=Rect(320,80,35,35) #fill paint
polygonToolRect=Rect(461,80,35,35) #polygon tool
shapeFillRect=Rect(439,30,85,35) #shape Fill
copyRect=Rect(620,100,40,40) #copy Rect
loadButtonRect=Rect(20,30,51,70) #loadButton
saveButtonRect=Rect(82,30,51,70) #saveButton
undoRect=Rect(15,105,30,30) #undoRect
redoRect=Rect(105,105,30,30) #redoRect
copyRect=Rect(60,105,30,30) #copyRect
squareToolRect=Rect(389,80,35,35) #crayon Tool (used to be for square)

#Stamp Rects
stamp1Rect=Rect(608,30,35,35)
stamp2Rect=Rect(658,30,35,35)
stamp3Rect=Rect(708,30,35,35)
stamp4Rect=Rect(608,80,35,35)
stamp5Rect=Rect(658,80,35,35)
stamp6Rect=Rect(708,80,35,35)

#Background Rects
background1Rect=Rect(777,30,100,40)
background2Rect=Rect(777,80,100,40)
background3Rect=Rect(887,30,100,40)
background4Rect=Rect(887,80,100,40)
background5Rect=Rect(997,30,100,40)
background6Rect=Rect(997,80,100,40)

#color Rects
color1PicRect=Rect(1290,15,20,20)
color2PicRect=Rect(1290,45,20,20)
color3PicRect=Rect(1290,75,20,20)
color4PicRect=Rect(1290,105,20,20)
colorPaletteRect=Rect(1330,20,100,100)

#Music Rects
backSongRect=Rect(111,779,19,19)
middleSongRect=Rect(164,780,15,19)
nextSongRect=Rect(211,779,19,19)


thickness=1 #thickness
UndoList=[] #undoList
RedoList=[] #redoList
coordinates=[]#used for polygon
storage=[]#used to store points so that when right click happens you can connect
#last and first
coords=[] #coordinates for polygonTool and more!

#Images Loads

backgroundPic=image.load("images/thebackground.png")

#Christmas Lights
lights0=image.load("images/lights0.png")
lights1=image.load("images/lights1.png")
lights2=image.load("images/lights2.png")

#Stamp Pic Loads
stampPicturesLoad=["images/stamp1.png","images/stamp2.png","images/stamp3.png","images/stamp4.png","images/stamp5.png","images/stamp6.png"]
stampPics=[]
for i in stampPicturesLoad:
    stampLoad=image.load(i)
    stampPics.append(stampLoad)
'''
stamp1Pic=image.load("images/stamp1.png")
stamp2Pic=image.load("images/stamp2.png")
stamp3Pic=image.load("images/stamp3.png")
stamp4Pic=image.load("images/stamp4.png")
stamp5Pic=image.load("images/stamp5.png")
stamp6Pic=image.load("images/stamp6.png")
'''

#Background Pic Loads
background1=image.load("images/background1.png")
background2=image.load("images/background2.png")
background3=image.load("images/background3.png")
background4=image.load("images/background4.png")
background5=image.load("images/background5.png")
background6=image.load("images/background6.png")
background1UnHovered=image.load("images/background1UnHovered.png")
background2UnHovered=image.load("images/background2UnHovered.png")
background3UnHovered=image.load("images/background3UnHovered.png")
background4UnHovered=image.load("images/background4UnHovered.png")
background5UnHovered=image.load("images/background5UnHovered.png")
background6UnHovered=image.load("images/background6UnHovered.png")
background1Hovered=image.load("images/background1Hovered.png")
background2Hovered=image.load("images/background2Hovered.png")
background3Hovered=image.load("images/background3Hovered.png")
background4Hovered=image.load("images/background4Hovered.png")
background5Hovered=image.load("images/background5Hovered.png")
background6Hovered=image.load("images/background6Hovered.png")

#Color Palletes
colorCircle1UnHovered=image.load("images/colorCircle1UnHovered.png")
colorCircle2UnHovered=image.load("images/colorCircle2UnHovered.png")
colorCircle3UnHovered=image.load("images/colorCircle3UnHovered.png")
colorCircle4UnHovered=image.load("images/colorCircle4UnHovered.png")
colorCircle1Hovered=image.load("images/colorCircle1Hovered.png")
colorCircle2Hovered=image.load("images/colorCircle2Hovered.png")
colorCircle3Hovered=image.load("images/colorCircle3Hovered.png")
colorCircle4Hovered=image.load("images/colorCircle4Hovered.png")


#ALL BUTTON PICTURE LOADS
loadButtonUnHovered=image.load("images/loadButtonUnHovered.png")
loadButtonHovered=image.load("images/loadButtonHovered.png")
saveButtonUnHovered=image.load("images/saveButtonUnHovered.png")
saveButtonHovered=image.load("images/saveButtonHovered.png")
undoButtonUnHovered=image.load("images/undoButtonUnHovered.png")
undoButtonHovered=image.load("images/undoButtonHovered.png")
redoButtonUnHovered=image.load("images/redoButtonUnHovered.png")
redoButtonHovered=image.load("images/redoButtonHovered.png")
copyButtonUnHovered=image.load("images/copyButtonUnHovered.png")
copyButtonHovered=image.load("images/copyButtonHovered.png")
pencilButtonUnHovered=image.load("images/pencilButtonUnHovered.png")
pencilButtonHovered=image.load("images/pencilButtonHovered.png")
eraserButtonUnHovered=image.load("images/eraserButtonUnHovered.png")
eraserButtonHovered=image.load("images/eraserButtonHovered.png")
highlighterButtonUnHovered=image.load("images/highlighterButtonUnHovered.png")
highlighterButtonHovered=image.load("images/highlighterButtonHovered.png")
fountainPenButtonUnHovered=image.load("images/fountainPenButtonUnHovered.png")
fountainPenButtonHovered=image.load("images/fountainPenButtonHovered.png")
sprayPaintButtonUnHovered=image.load("images/sprayPaintButtonUnHovered.png")
sprayPaintButtonHovered=image.load("images/sprayPaintButtonHovered.png")
colourPickerButtonUnHovered=image.load("images/colourPickerButtonUnHovered.png")
colourPickerButtonHovered=image.load("images/colourPickerButtonHovered.png")
brushButtonUnHovered=image.load("images/brushButtonUnHovered.png")
brushButtonHovered=image.load("images/brushButtonHovered.png")
fillPaintButtonUnHovered=image.load("images/fillPaintButtonUnHovered.png")
fillPaintButtonHovered=image.load("images/fillPaintButtonHovered.png")
rectButtonUnHovered=image.load("images/rectButtonUnHovered.png")
rectButtonHovered=image.load("images/rectButtonHovered.png")
shapeFillButtonUnHovered=image.load("images/shapeFillButtonUnHovered.png")
shapeFillButtonHovered=image.load("images/shapeFillButtonHovered.png")
shapeFilledButtonUnHovered=image.load("images/shapeFilledButtonUnHovered.png")
shapeFilledButtonHovered=image.load("images/shapeFilledButtonHovered.png")
ellipseButtonUnHovered=image.load("images/ellipseButtonUnHovered.png")
ellipseButtonHovered=image.load("images/ellipseButtonHovered.png")
squareButtonUnHovered=image.load("images/squareButtonUnHovered.png")
squareButtonHovered=image.load("images/squareButtonHovered.png")
polygonButtonUnHovered=image.load("images/polygonButtonUnHovered.png")
polygonButtonHovered=image.load("images/polygonButtonHovered.png")
lineButtonUnHovered=image.load("images/lineButtonUnHovered.png")
lineButtonHovered=image.load("images/lineButtonHovered.png")
stamp1ButtonUnHovered=image.load("images/stamp1ButtonUnHovered.png")
stamp1ButtonHovered=image.load("images/stamp1ButtonHovered.png")
stamp2ButtonUnHovered=image.load("images/stamp2ButtonUnHovered.png")
stamp2ButtonHovered=image.load("images/stamp2ButtonHovered.png")
stamp3ButtonUnHovered=image.load("images/stamp3ButtonUnHovered.png")
stamp3ButtonHovered=image.load("images/stamp3ButtonHovered.png")
stamp4ButtonUnHovered=image.load("images/stamp4ButtonUnHovered.png")
stamp4ButtonHovered=image.load("images/stamp4ButtonHovered.png")
stamp5ButtonUnHovered=image.load("images/stamp5ButtonUnHovered.png")
stamp5ButtonHovered=image.load("images/stamp5ButtonHovered.png")
stamp6ButtonUnHovered=image.load("images/stamp6ButtonUnHovered.png")
stamp6ButtonHovered=image.load("images/stamp6ButtonHovered.png")

#Color Wheel Pic Load
colorWheelRect=Rect(1180,20,100,100)
colorCirclePic1=image.load("images/colorCircle1.png")
colorCirclePic2=image.load("images/colorCircle2.png")
colorCirclePic3=image.load("images/colorCircle3.png")
colorCirclePic4=image.load("images/colorCircle4.png")

#SONG BUTTON LOADS
backButtonUnHovered=image.load("images/backButtonUnHovered.png")
playButtonUnHovered=image.load("images/playButtonUnHovered.png")
nextButtonUnHovered=image.load("images/nextButtonUnHovered.png")
backButtonHovered=image.load("images/backButtonHovered.png")
playButtonHovered=image.load("images/playButtonHovered.png")
nextButtonHovered=image.load("images/nextButtonHovered.png")
musicUpButtonUnHovered=image.load("images/musicUpButtonUnHovered.png")
musicUpButtonHovered=image.load("images/musicUpButtonHovered.png")
musicDownButtonUnHovered=image.load("images/musicDownButtonUnHovered.png")
musicDownButtonHovered=image.load("images/musicDownButtonHovered.png")

#Another Music Pic Loads
musicPlayer1=image.load("images/musicplayer1.png")
musicPlayer2=image.load("images/musicplayer2.png")
musicPlayer22=image.load("images/musicplayer22.png")
musicPlayer3=image.load("images/musicplayer3.png")
musicPlayer33=image.load("images/musicplayer33.png")
musicPlayer4=image.load("images/musicplayer4.png")
musicPlayer44=image.load("images/musicplayer44.png")

screen.blit(backgroundPic,(0,0)) #blitting the white background

toolHovered="Nothing Selected!" #Hovering Text, setting as "Nothing Selected!"

myText="0" #my coords; setting as 0
draw.rect(screen,WHITE,canvasRect)#drawing the canvas BEFORE THE LOOP
draw.rect(screen,(30,30,30),(0,0,1470,140)) #GREY RECTANGLE 

unFilledRect=screen.subsurface(canvasRect).copy() #taking a screen shot

omx,omy,mx,my=0,0,0,0 #everything set as 0

col=BLACK #default colour

lightsNum=1 #for Christmas Lights; the number
volume=mixer.music.get_volume() #getting the volume

#BackgroundLists
background=1 #background number
backgroundPic=1 #background number picture
picnames=["images/background1.png","images/background2.png","images/background3.png","images/background4.png","images/background5.png","images/background6.png"] #all the backgroundPics, getting loaded
texture=[] #used for erasing
for name in picnames: #its able to load and list any picture from the picnames list
    pic=image.load(name) #loads the background pictures
    texture.append(pic) #adds the picture to the texture list; used for eraser

pos=0 #position for erasrr
n=len(texture) #for length of texture

UndoList=[] #UndoList adding the first background

colorWheel=0 #colorWheel number set to 0

mxText="N/A" #mx coords set to N/A
myText="N/A" #my coords set to N/A

running=True 
tool="" #setting tool as no tool for now
copymx=[] #for copy Tool; X
copymy=[] # for copy Tool; Y
copyNum=1 #copy Number

song=0 #song number as 0
songNumber=0 #song number as 0
pauseSong=False #pauseSong=False
tarj=0 #used for scrubbing; its finds the coordinates
musicDownRect=Rect(79,779,19,19) #musicDown Rect
musicUpRect=Rect(250,779,19,19) #musicUp Rect

print("Copyright (c) 2020 Tarj Mecwan. All rights reserved.") 
print("Permission is hereby granted to modify and redistribute this program for educational purposes with attribution.")

display.set_caption('Paint Project - Stranger Things')
while running:
    if backgroundPic==1: #if backgroundPic ==1
        tool="" #setting tool is nothing
        screen.blit(background1,(0,140)) #blitting the background
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy() 
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
            #Appending this screenshot to the undoList
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools
    elif backgroundPic==2: #if backgroundPic==2
        tool="" #setting tool is nothing
        screen.blit(background2,(0,0)) #blitting the background
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy()
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools
    elif backgroundPic==3: #if backgroundPic==3
        tool="" #setting tool to nothing
        screen.blit(background3,(0,0))
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy() 
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
            #Appending this screenshot to the undoList
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools
    elif backgroundPic==4:
        tool=""
        screen.blit(background4,(0,0))
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy() 
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
            #Appending this screenshot to the undoList
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools
    elif backgroundPic==5:
        tool=""
        screen.blit(background5,(0,0))
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy() 
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
            #Appending this screenshot to the undoList
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools
    elif backgroundPic==6:
        tool=""
        screen.blit(background6,(0,0))
        draw.rect(screen,(30,30,30),(0,0,1470,140)) #blitting the grey rect
        capture=screen.subsurface(0,140,1470,534).copy() 
            #I am appending it when the canvasRect is being touched
        UndoList.append(capture)
            #Appending this screenshot to the undoList
        backgroundPic=7 #setting the background to 7; so its not repeated over and over again
        unFilledRect=screen.subsurface(canvasRect).copy() #unFilledRect; is a name I called accidently! Its for all the tools

#CHRISTMAS LIGHTS //ITS BASICALLY A HUGE LOOP/TIMER
    if lightsNum>=200:
        lightsNum=0
    elif lightsNum<201:
        lightsNum=lightsNum+1
    if lightsNum==100:
        screen.blit(lights1,(0,140)) # print image
    elif lightsNum==200:
        screen.blit(lights2,(0,140)) #print image
        
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN: #mousedown evt.type
            if evt.button==4: #if you scroll DOWN
                if thickness>1:
                    thickness-=1
                del UndoList[-1]
            if evt.button==5: #if you scroll UP
                if tool=="pencil": #restriction on tool=pencil
                    if thickness<7:
                        thickness+=1
                    elif thickness>=7:
                        thickness=7
                elif tool=="rectangle": #restriction on tool=rectangle
                    if thickness<50:
                        thickness+=1
                    elif thickness>=50:
                        thickness=50
                elif thickness<50:
                    thickness+=1
                del UndoList[-1] #deletes the last undolist that is added when scrolling
            if musicChangerRect.collidepoint(mx,my): 
                musicPosition=mx-60 #to get the musicposition relative to music scrubber
                try:
                    mixer.music.set_pos(musicPosition) #setting the position
                    tarj=(60+3*round(mixer.music.get_pos()/1000))-musicPosition-60 #getting the music's position than subtracting from music position
                except: #except
                    pass #pass
            if tool=="copyTool" and canvasRect.collidepoint(mx,my): #if the tool is copyTool and canvasRect collidedpoint
                copymx.append(mx) #append the mx coord
                copymy.append(my) #append the my coord
            sx,sy=evt.pos #sx,sy position
            if shapeFillRect.collidepoint(mx,my):#shapeFill collide
                if shapeFill==True: #if shapeFill == True
                    shapeFill=False #then shapefill = false
                elif shapeFill==False: #shapefill == false
                    shapeFill=True #then shapefill = true
            if nextSongRect.collidepoint(mx,my): 
                songNumber+=1 #adds integer to songNumber
                if songNumber==1:
                    song=1
                if songNumber==2:
                    song=2
                if songNumber==3:
                    songNumber=3
                    song=3
                if songNumber>=4: #basic loop for only 3 songs
                    songNumber=1
                    song=1
            if backSongRect.collidepoint(mx,my):
                songNumber-=1 #removes integer to songNumber
                if songNumber==1:
                    song=1
                if songNumber==2:
                    song=2
                if songNumber==3:
                    songNumber=3
                    song=3
                if songNumber<=0: #basic loop for only 3 songs
                    songNumber=3
                    song=3 
            if middleSongRect.collidepoint(mx,my):
                if pauseSong==False:
                    mixer.music.pause() #pause song
                    pauseSong=True
                elif pauseSong==True:
                    mixer.music.unpause() #unpause song
                    pauseSong=False
            if musicDownRect.collidepoint(mx,my):
                volume=volume-0.05 #volume down; substracting by 0.05
                if volume<=0: #if volume is less than 0
                    volume=0 #volume is 0
                mixer.music.set_volume(volume) #setting the volume
            if musicUpRect.collidepoint(mx,my):
                volume=volume+0.05 #volume up; adding by 0.05
                if volume>=1: #if more than 1
                    volume=1 #volume = 1
                mixer.music.set_volume(volume) #setting the volume
            #screen.blit(stamp1Pic,(mx-50,my-67))
            if tool=="polygonTool" and canvasRect.collidepoint(mx,my):
                position=mx,my
                #appending the positions to 2 lists
                coordinates.append(position)
                storage.append(position)#to store coordinates
                coords.append(position)
            if polygonToolRect.collidepoint(mx,my):#polygon code
                if evt.button==3:#if right click
                    coords=[]
                    #connecting last and first points with the storage loop
                    draw.line(screen,col,(storage[-1]),(storage[0]),thickness) 
                    if len(coords)>=3:
                        for x in range(40):
                            coords.append(coords[0]) #appends first coord for any complications
                        if shapeFill==False:
                            draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],thickness)
                        if shapeFill==True:
                            draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],0)
                    coordinates=[]#clearing the two lists so that it can restart count
                    storage=[] #cleares all lists
                    coords=[] #cleares all lists
            if undoRect.collidepoint(mx,my):#touching undo rectangle
                #kept on appending last element to redo list
                #while deleting last undo list element while
                #bliting last image unless if it is 1 length of the list
                tool=""
                if len(UndoList)>=2:#if list is 2 or greater
                    #screen.blit(screenShot,(0,0))
                    RedoList.append(UndoList[-1])#add undolist's last element to redolist
                    screen.blit(UndoList[-2],(0,140))#put UndoList's last element on the screen
                    del UndoList[-1]#delete undoList last element
                    
                
                if len(UndoList)==1:
                    #RedoList.append(UndoList[0])#0 since it is the only element
                    #del UndoList[0]#deleting it
                    screen.set_clip(canvasRect)#only the canvas can be "updated"
                    screen.fill(WHITE)

            if redoRect.collidepoint(mx,my):#redo
                #similar to the undoRect code
                #seperate if statement for 1 because I can't blit -2 when
                #there is only one element. It will crash then.
                if len(RedoList)==1:
                    screen.blit(RedoList[-1],(0,140))
                    UndoList.append(RedoList[-1])#appending to undo
                    del RedoList[-1]#delete it and make it an empty list

                if len(RedoList)>=2:
                    #screen.blit(screenShot,(0,0))
                    screen.blit(RedoList[-1],(0,140))#-2 since it is 2nd last element
                    UndoList.append(RedoList[-1])
                    del RedoList[-1] #deletes last element from redolist
        if evt.type==MOUSEBUTTONUP: #mousebutton up evt.type
            if tool=="copyTool" and canvasRect.collidepoint(mx,my): #for tool="copy
                copymx.append(mx) #appends mx coord
                copymy.append(my) #append my cord
                copyNum=2 #for copy Checker; needed for the program!
            if background1Rect.collidepoint(mx,my): #background 1
                background=1
                backgroundPic=1
            if background2Rect.collidepoint(mx,my): #background 2
                background=2
                backgroundPic=2
            if background3Rect.collidepoint(mx,my): #background 3
                background=3
                backgroundPic=3
            if background4Rect.collidepoint(mx,my): #background 4
                background=4
                backgroundPic=4
            if background5Rect.collidepoint(mx,my): #background 5
                background=5
                backgroundPic=5
            if background6Rect.collidepoint(mx,my): #background 6
                background=6
                backgroundPic=6
            if saveButtonRect.collidepoint(mx,my):
                try:
                   fname=filedialog.asksaveasfilename(defaultextension=".png") #gets the final name; default extension .png
                   image.save(unFilledRect.copy(),fname) #image save
                except:
                    print("Saving error!")
            if loadButtonRect.collidepoint(mx,my):
                try:
                    background=1 #background=1 to make it white
                    draw.rect(screen,WHITE,canvasRect) #also adds the canvas Rect (WHITE); just so everything clears off
                    fname=filedialog.askopenfilename() #fname is a string tha has the full path of the selected file
                    myPic=image.load(fname) #loads the file
                    cw=myPic.get_width() #gets the width
                    ch=myPic.get_height() #gets the height
                    if cw>=1470: #if width is over 1740
                        cw=1470 #make width to 1470
                    if ch>=533: #if height is over 533
                        ch=533 #make height to 533
                    myPicPic=transform.scale(myPic,(cw,ch)) #transform if the picture is bigger than canvas
                    screen.blit(myPicPic,(0,140)) #blitting the picture
                    capture=screen.subsurface(0,140,1470,534).copy() #screenshots the cavas
                    UndoList.append(capture) #appends it
                except:
                    print("LOAD ERROR!")
            if polygonToolRect.collidepoint(mx,my):#polygon code
                if evt.button==3:#if right click
                    #connecting last and first points with the storage loop
                    draw.line(screen,col,(storage[-1]),(storage[0]),5) 
                    if len(coords)>=3: #if the you have more than 3 coords
                        for x in range(40): 
                            coords.append(coords[0]) #appends first coord to reduce complications
                        if shapeFill==False: #fill off
                            draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],thickness)
                        if shapeFill==True: #fill on
                            draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],0)
                    coords=[] #clears the list
                    coordinates=[]#clearing the two lists so that it can restart count
                    storage=[] #clears the list
            if tool=="rectangle": #rectangle tool
                if shapeFill==False: #if shape fill is off
                    screen.set_clip(canvasRect) #set clip to only canvasRect
                    for x in range(thickness): #only for thickness
                        draw.rect(screen,col,(sx+thickness,sy+x,mx-sx,my-sy),1) #1 side
                        draw.rect(screen,col,(sx+x,sy+thickness,mx-sx,my-sy-1),1)#2 side
                        draw.rect(screen,col,(sx+x,sy,mx-sx,my-sy),1)#3 side
                        draw.rect(screen,col,(sx,sy,thickness-1,thickness))#4 side
                        if mx<=sx: #needed to remove the transparent box
                            draw.rect(screen,col,(mx,my,thickness+1,thickness-1)) #adds the rectangle to do it
                if shapeFill==True: #if shape fill is on
                    screen.set_clip(canvasRect) #set clip to only canvas rect
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy)) #draw the rect unfilled
            if tool=="ellipse": #ellipse
                if shapeFill==True: #if shape fill is on
                    screen.set_clip(canvasRect) #set clip to only canvasrect
                    try: 
                        ellRect=Rect(sx,sy,mx-sx,my-sy) #getting the coordinate; rectangle
                        ellRect.normalize()#no more negative errors!
                        draw.ellipse(screen,col,ellRect) #draw it, but for ellipses
                    except:
                        print("negative radius")
                        print("mouse up - screen shot")
                if shapeFill==False: #if shape fill is off
                    for i in range(thickness): #only for thickness
                        screen.set_clip(canvasRect) #set clip to canvas rect
                        try:
                            #THE FOUR DRAW.ELLIPSES AFTER EACH CASE MEANS THAT THE ELLIPSE IS WRONG UP 1 or DOWN 1 ON EACH SIDE. I didn't comment since it's super repetative. Message me if you do need me to explain the code to you
                            if sx<mx and sy<my: #case 1
                                draw.ellipse(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1) #case 1 ellipse
                                if thickness>1:
                                    draw.ellipse(screen,col,(sx-i+1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(sx-i-1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(sx-i+1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(sx-i-1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                            if sx>mx and sy>my: #case 2
                                draw.ellipse(screen,col,(mx-i,my-i,sx-mx+i*2,sy-my+i*2),1) #case 2 ellipse
                                if thickness>1:
                                    draw.ellipse(screen,col,(mx-i+1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(mx-i-1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(mx-i+1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(mx-i-1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                            if sx<mx and sy>my: #case 3
                                draw.ellipse(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1) #case 3 ellipse
                                if thickness>1:
                                    draw.ellipse(screen,col,(sx-i+1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(sx-i-1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(sx-i+1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                    draw.ellipse(screen,col,(sx-i-1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                            if sx>mx and sy<my: #case 4
                                draw.ellipse(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1) #case 4 ellipse
                                if thickness>1:
                                    draw.ellipse(screen,col,(mx-i+1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(mx-i-1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(mx-i+1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                    draw.ellipse(screen,col,(mx-i-1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)   
                        except:
                            pass 
            if tool=="line": #line tool
                screen.set_clip(canvasRect) #set clip to canvas rect
                draw.line(screen,col,(sx,sy),(mx,my),thickness) #draw the line
                    
        if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my): #if the mousebutton up and the canvas rect collide as well
            capture=screen.subsurface(0,140,1470,534).copy() 
                #I am appending it when the canvasRect is being touched
            UndoList.append(capture)
                #Appending this screenshot to the undoList

            unFilledRect=screen.subsurface(canvasRect).copy()
            
        if evt.type==KEYDOWN: #if you press a key down
            if evt.key==K_f: #if you press K
                if shapeFill==True:
                    shapeFill=False
                elif shapeFill==False:
                    shapeFill=True
                        
            unFilledRect=screen.subsurface(canvasRect).copy()
            
    mx,my=mouse.get_pos()#current mouse position
    mb=mouse.get_pressed() #left/middle/right click

    #drawing all tools
    imageNamesCoords=[(777,30),(777,80),(887,30),(887,80),(997,30),(997,80),(170,30),(220,30),(270,30),(320,30),(170,80),(220,80),(270,80),(320,80),(389,30),(439,30),(539,30),(389,80),(461,80),(539,80),(608,30),(658,30),(708,30),(608,80),(658,80),(708,80),(1290,15),(1290,45),(1290,75),(1290,105),(111,779),(164,780),(211,779),(78,779),(250,779),(60,105)] #coordinates for each blit
    imageNames=[background1UnHovered,background2UnHovered,background3UnHovered,background4UnHovered,background5UnHovered,background6UnHovered,pencilButtonUnHovered,eraserButtonUnHovered,highlighterButtonUnHovered,fountainPenButtonUnHovered,sprayPaintButtonUnHovered,colourPickerButtonUnHovered,brushButtonUnHovered,fillPaintButtonUnHovered,rectButtonUnHovered,shapeFillButtonUnHovered,ellipseButtonUnHovered,squareButtonUnHovered,polygonButtonUnHovered,lineButtonUnHovered,stamp1ButtonUnHovered,stamp2ButtonUnHovered,stamp3ButtonUnHovered,stamp4ButtonUnHovered,stamp5ButtonUnHovered,stamp6ButtonUnHovered,colorCircle1UnHovered,colorCircle2UnHovered,colorCircle3UnHovered,colorCircle4UnHovered,backButtonUnHovered,playButtonUnHovered,nextButtonUnHovered,musicDownButtonUnHovered,musicUpButtonUnHovered,copyButtonUnHovered] #all image names
    for i in range(len(imageNames)): #for i in range for the lengthh of a lost
        screen.blit(imageNames[i],imageNamesCoords[i]) #screen.blit all the images
    
    #middle lines
    draw.line(screen,GREY,(150,20),(150,120),2)
    draw.line(screen,GREY,(372,20),(372,120),2)
    draw.line(screen,GREY,(591,20),(591,120),2)
    draw.line(screen,GREY,(760,20),(760,120),2)
    draw.line(screen,GREY,(1114,20),(1114,120),2)
    

    #SIX PRIMARY COLOURS
    draw.rect(screen,(0,255,255),(1330,20,30,30))
    draw.rect(screen,(255,0,0),(1365,20,30,30))
    draw.rect(screen,(128,0,128),(1400,20,30,30))
    draw.rect(screen,GREEN,(1330,55,30,30))
    draw.rect(screen,(0,0,0),(1365,55,30,30))
    draw.rect(screen,(255,192,203),(1400,55,30,30))
    draw.rect(screen,(0,0,255),(1330,90,30,30))
    draw.rect(screen,(255,255,255),(1365,90,30,30))
    draw.rect(screen,(255,255,102),(1400,90,30,30))
    
    #selecting the tools
    if mb[0]==1 and pencilRect.collidepoint(mx,my):
        tool="pencil"
    if mb[0]==1 and eraserRect.collidepoint(mx,my):
        tool="eraser"
    if mb[0]==1 and highlighterRect.collidepoint(mx,my):
        tool="highlighter"
    if mb[0]==1 and rectangleToolRect.collidepoint(mx,my):
        tool="rectangle"
    if mb[0]==1 and ellipseToolRect.collidepoint(mx,my):
        tool="ellipse"
    if mb[0]==1 and fountainPenRect.collidepoint(mx,my):
        tool="fountainPen"
    if mb[0]==1 and lineToolRect.collidepoint(mx,my):
        tool="line"
    if mb[0]==1 and sprayPaintToolRect.collidepoint(mx,my):
        tool="sprayPaint"
    if mb[0]==1 and brushToolRect.collidepoint(mx,my):
        tool="brush"
    if mb[0]==1 and colourPickerToolRect.collidepoint(mx,my):
        tool="colourPicker"
    if mb[0]==1 and polygonToolRect.collidepoint(mx,my):
        tool="polygonTool"
    if mb[0]==1 and copyRect.collidepoint(mx,my):
        tool="copyTool"
    if mb[0]==1 and fillPaintToolRect.collidepoint(mx,my):
        tool="fillPaint"
    if mb[0]==1 and squareToolRect.collidepoint(mx,my):
        tool="square"
    if mb[0]==1 and stamp1Rect.collidepoint(mx,my):
        tool="stamp1"
        stampPosition=0 #setting the position for the stamp
    if mb[0]==1 and stamp2Rect.collidepoint(mx,my):
        tool="stamp2"
        stampPosition=1#setting the position for the stamp
    if mb[0]==1 and stamp3Rect.collidepoint(mx,my):
        tool="stamp3"
        stampPosition=2 #setting the position for the stamp
    if mb[0]==1 and stamp4Rect.collidepoint(mx,my):
        tool="stamp4"
        stampPosition=3 #setting the position for the stamp
    if mb[0]==1 and stamp5Rect.collidepoint(mx,my):
        tool="stamp5"
        stampPosition=4 #setting the position for the stamp
    if mb[0]==1 and stamp6Rect.collidepoint(mx,my):
        tool="stamp6"
        stampPosition=5 #setting the position for the stamp
    if mb[0]==1 and color1PicRect.collidepoint(mx,my):
        colorWheel=1
    if mb[0]==1 and color2PicRect.collidepoint(mx,my):
        colorWheel=2
    if mb[0]==1 and color3PicRect.collidepoint(mx,my):
        colorWheel=3
    if mb[0]==1 and color4PicRect.collidepoint(mx,my):
        colorWheel=4
        
    if tool=="polygonTool" and mb[2]==1:#right click and tool is polygon
        if len(storage)<3:#or else program will crash
            pass #passing since nothing happens
        elif len(storage)>2:#when it is 3 or greater than we do 
            draw.line(screen,col,(storage[-2]),(storage[0]),thickness)#we connect the last point and the first point
            if len(coords)>=3: #only if coordinate list is 3 to more
                coords.pop(-1) #removes the last coordinate
                for x in range(40):  #keeps added til 40 times
                    coords.append(coords[0]) #appends first coordinate to reduce complications
                if shapeFill==False:
                    draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],thickness)
                if shapeFill==True:
                    draw.polygon(screen,col,[coords[0],coords[1],coords[2],coords[3],coords[4],coords[5],coords[6],coords[7],coords[8],coords[9],coords[10],coords[11],coords[12],coords[13],coords[14],coords[15],coords[16],coords[17],coords[18],coords[19],coords[20],coords[21],coords[22],coords[23],coords[25],coords[26],coords[27],coords[28],coords[29],coords[30],coords[0]],0)
            storage=[] #clears list
            coords=[] #clears list
            coordinates=[]#we clear coordinates and storage lists so that we can restart the points and everything is performed in another fresh way
    #using the tools
    if mb[0]==1:# and canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect) #sets clip to canvas rect only
        if tool=="pencil": #pencil
            toolHovered="Pencil" #tool hovered
            if thickness>9: #if the thickness is more than 9
                thickness=7 #sets to 8
            draw.line(screen,col,(omx,omy),(mx,my),thickness) #draw the pencil line
        if tool=="eraser": #eraser
            toolHovered="Eraser" #tool hovered
            if background==1: #if the background is 1
                pos=0 #position is 0
                dx=mx-omx #gets the dx from the mx and omx
                dy=my-omy #gets the dy from the my and omy
                dist=sqrt(dy**2+dy**2) #gets the distance
                draw.circle(screen,WHITE,(mx,my),thickness) #draws the circles
            #MAKES IT SO THERE ISN'T ANY HOLES WHEN DRAWING (ERASER)
                for i in range(1,int(dist)): 
                    cx=int(omx+i*dx/dist)
                    cy=int(omy+i*dy/dist)
                    draw.circle(screen,WHITE,(cx,cy),thickness)
            if background==2: #if background =2
                pos=1 #position = 1
            elif background==3: #if background = 3
                pos=2 #position = 2
            elif background==4: #if background = 4
                pos=3 #position = 3
            elif background==5: #if background = 5
                pos=4 #position = 4
            elif background==6: #if background = 6
                pos=5 #position = 5
            try:
                if pos==0 or pos==1 or pos==2 or pos==3 or pos==4 or pos==5:
                    sample=texture[pos].subsurface(mx-thickness/2,my-thickness/2,thickness,thickness) #gets thee sample from the position
                    screen.blit(sample,(mx-thickness/2,my-thickness/2)) #blits the eraser from the background
            except:
                pass
        if tool=="highlighter": #highlighter
            toolHovered="Highlighter" #tool hovered
            screen.blit(unFilledRect,canvasRect) #blits the picture; unfilledrect
                #when using highlighter there are 4 elements in a color. Last element is transparency. You have to use first 3 to know the color
            a=col
            first=a[0]
            second=a[1]
            third=a[2]
                #now I got the color
              
            highlighter=Surface((60,60),SRCALPHA)#making a blank surface
            
            draw.circle(highlighter,(first,second,third,20),(thickness//2,thickness//2),thickness)#draw a first circle so that the first mark is made
                #the 20 is the transparency
            dx=mx-omx#horizontal distance (run)
            dy=my-omy#vertical distance (rise)
                #marker=Surface((60,60),SRCALPHA)#making a blank surface
                #brush code now
            dist=int(sqrt(dx**2+dy**2))
            for i in range(1,dist+1):#1,2,3......
                dotX=int(omx+i*dx/dist)
                dotY=int(omy+i*dy/dist)
                if mx!=omx or my!=omy:#there is movement
                    screen.blit(highlighter,(dotX-thickness/2,dotY-thickness/2))
                        #It is important to blit it and not just draw it. You are just bliting the image and it works fine.
            unFilledRect=screen.subsurface(canvasRect).copy()
        if tool=="rectangle": #rectangle
            toolHovered="Rectangle Tool" #tool hovered
            screen.blit(unFilledRect,canvasRect) #screen blit the unfilled rect
            if shapeFill==False: 
                if mb[0]==1:
                    for x in range(thickness):
                        draw.rect(screen,col,(sx+thickness,sy+x,mx-sx,my-sy),1) #case 1
                        draw.rect(screen,col,(sx+x,sy+thickness,mx-sx,my-sy-1),1) #case 2
                        draw.rect(screen,col,(sx+x,sy,mx-sx,my-sy),1) #case 3
                        draw.rect(screen,col,(sx,sy,thickness,thickness)) #case 4
                        if mx<=sx: #used to add the transparent rectangle
                            draw.rect(screen,col,(mx,my,thickness,thickness-1)) #draws the rectangle
            if shapeFill==True: 
                if mb[0]==1:
                    draw.rect(screen,col,(sx,sy,mx-sx,my-sy)) #draws the filled rect
        if tool=="ellipse": #ellipse
            toolHovered="Ellipse Tool" #tool hovered
            screen.blit(unFilledRect,canvasRect)
            if shapeFill==True:
                try:
                    ellRect=Rect(sx,sy,mx-sx,my-sy)
                    ellRect.normalize()#no more negative errors!
                    draw.ellipse(screen,col,ellRect)
                except:
                    print("negative radius")
            if shapeFill==False:
                for i in range(thickness):
                    screen.set_clip(canvasRect)
                    try:
                        #THE FOUR DRAW.ELLIPSES AFTER EACH CASE MEANS THAT THE ELLIPSE IS WRONG UP 1 or DOWN 1 ON EACH SIDE. I didn't comment since it's super repetative. Message me if you do need me to explain the code to you
                        if sx<mx and sy<my: #case 1
                            draw.ellipse(screen,col,(sx-i,sy-i,mx-sx+i*2,my-sy+i*2),1) #case 1 ellipse
                            if thickness>1:
                                draw.ellipse(screen,col,(sx-i+1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i+1,sy-i-1,mx-sx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,sy-i+1,mx-sx+i*2,my-sy+i*2),1)
                        if sx>mx and sy>my: #case 2
                            draw.ellipse(screen,col,(mx-i,my-i,sx-mx+i*2,sy-my+i*2),1) #case 2 ellipse
                            if thickness>1:
                                draw.ellipse(screen,col,(mx-i+1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i+1,my-i-1,sx-mx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,my-i+1,sx-mx+i*2,sy-my+i*2),1)
                        if sx<mx and sy>my: #case 3
                            draw.ellipse(screen,col,(sx-i,my-i,mx-sx+i*2,sy-my+i*2),1) #case 3 ellipse
                            if thickness>1:
                                draw.ellipse(screen,col,(sx-i+1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i+1,my-i-1,mx-sx+i*2,sy-my+i*2),1)
                                draw.ellipse(screen,col,(sx-i-1,my-i+1,mx-sx+i*2,sy-my+i*2),1)
                        if sx>mx and sy<my: #case 4
                            draw.ellipse(screen,col,(mx-i,sy-i,sx-mx+i*2,my-sy+i*2),1) #case 4 ellipse
                            if thickness>1:
                                draw.ellipse(screen,col,(mx-i+1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i+1,sy-i-1,sx-mx+i*2,my-sy+i*2),1)
                                draw.ellipse(screen,col,(mx-i-1,sy-i+1,sx-mx+i*2,my-sy+i*2),1)  
                    except:
                        pass      
        if tool=="fountainPen": #fountain pen
            toolHovered="Fountain Pen" #tool hovered
            draw.polygon(screen,col,[(omx,omy-thickness),(omx,omy+thickness),(mx,my+thickness),(mx,my-thickness)]) #draws the polygon toward horizontal
        if tool=="line": #line
            toolHovered="Line Tool" #tool hovered
            screen.blit(unFilledRect,canvasRect) #blits the unfilled rect
            draw.line(screen,col,(sx,sy),(mx,my),thickness) #draws the line
        if tool=="sprayPaint": #spraypaint
            toolHovered="Spray Paint" #tool hovered
            radius=thickness 
            for i in range(100): #speed
                xRangeOfCircle=randint(mx-radius*2,mx+radius*2) #xrange
                yRangeOfCircle=randint(my-radius*2,my+radius*2) #yrange
                distance=sqrt(((mx-xRangeOfCircle)**2)+((my-yRangeOfCircle)**2)) #gets the distance
                if distance<=radius: #if the distance is less than the radius
                    draw.circle(screen,col,(xRangeOfCircle,yRangeOfCircle),0) #draw the small circles
        if tool=="brush": #brush
            toolHovered="Paint Brush" #tool hovered
            dx=mx-omx #dx
            dy=my-omy #dy
            dist=sqrt(dy**2+dy**2) #distance
            draw.circle(screen,col,(mx,my),thickness) #draw the circle

            for i in range(1,int(dist)): #len of distance
                cx=int(omx+i*dx/dist) #cx
                cy=int(omy+i*dy/dist) #cy
                draw.circle(screen,col,(cx,cy),thickness) #draws the circle; SAME AS ERASER (JUST DIFFERENT COLOUR)
        if tool=="colourPicker": #colour picker
            toolHovered="Colour Picker" #tool hovered
            if canvasRect.collidepoint(mx,my): #if collide point to canvasrect
                col=screen.get_at((mx,my)) #gets the colour
        if tool=="square": #crayon; yes it says square (USED TO BE SQUARE; UNTIL I CHANGE THE TOOL)
            toolHovered="Crayon" #tool hovered
            rx,ry=randint(-thickness,thickness),randint(-thickness,thickness) #random lines
            draw.line(screen,col,(mx-rx,my-ry),(mx-ry+1,my-ry+1)) # draws it
        if tool=="polygonTool":
            toolHovered="Polygon Tool"
            #We have used polygon a couple of times throughout the code. This part is so that the lines can be drawn.
            #For my polygon, I just drew lines connecting point to point
            #screen.blit(screenShot,(0,0))
            if len(coordinates)==2:#so that this is the first pair when you draw the first line. (0 and 1)
                draw.line(screen,col,(coordinates[0]),(coordinates[1]),thickness)
            if len(coordinates)>2:#this is after the first pair, you just keep on deleting the first element
                #this is why there was a storage list that was previously made
                del (coordinates[0])
                draw.line(screen,col,(coordinates[0]),(coordinates[1]),thickness)#just keeps on drawing these two parts of the coordinates

        if (tool=="stamp1" or tool=="stamp2" or tool=="stamp3" or tool=="stamp4" or tool=="stamp5" or tool=="stamp6")and canvasRect.collidepoint(mx,my): #if you press the stamp
            screen.blit(unFilledRect,(0,140)) #blits the unfilled rect image
            screen.blit(stampPics[stampPosition],(mx-50,my-67)) #blits the stamp
                                                                                                                                                 
        if tool=="fillPaint" and canvasRect.collidepoint(mx,my):  #paint bucket
            toolHovered="Paint Bucket" #tool hovered
            pixel=screen.get_at((mx,my)) #Colour of current pixel
            pixelList=[(mx,my)] #creates the list of coordinates

            if pixel !=col: #if the pixel colour is not equal to the current equal colour
                while len(pixelList) > 0: #stops errors and only goes until list is empty
                    if canvasRect.collidepoint(pixelList[0]) and screen.get_at(pixelList[0]) == pixel:
        
                        screen.set_at(pixelList[0],col)
                        #ALL GOES A DIFFERENT WAY
                        pixelList.append((pixelList[0][0],pixelList[0][1]+1)) #case 1; one way
                        pixelList.append((pixelList[0][0],pixelList[0][1]-1)) #case 2; one way
                        pixelList.append((pixelList[0][0]+1,pixelList[0][1])) #case3; one way
                        pixelList.append((pixelList[0][0]-1,pixelList[0][1])) #case 4; one way
                    del(pixelList[0])
        screen.set_clip(None)
    if tool=="copyTool" and canvasRect.collidepoint(mx,my): #copy tool
        toolHovered="Copy Tool" #tool hovered
        if copyNum==2: #if copynumber is 2
            pos1=copymx[0] #position 1
            pos2=copymy[0] #position 2
            pos3=copymx[1] #position 3
            pos4=copymy[1] #position 4
            try:
                if ((pos1**2+(pos2-140)**2)**1/2)<((pos3**2+(pos4-140)**2)**1/2): #up to down; H
                    capturepic=screen.subsurface(pos1,pos2,(pos3-pos1),(pos4-pos2)).copy() #captures the image
                    capturePic2=transform.scale(capturepic,(1470,534)) #transform it
                    screen.blit(capturePic2,(0,140)) #blits it
                    copymx=[] #clears the list 
                    copymy=[] #clears the list
                    copyNum=1
                elif ((pos1**2+(pos2-140)**2)**1/2)>((pos3**2+(pos4-140)**2)**1/2): #down to up; V
                    capturepic=screen.subsurface(pos3,pos4,(pos1-pos3),(pos2-pos4)).copy() #captures the image
                    capturePic2=transform.scale(capturepic,(1470,534)) #transform it
                    screen.blit(capturePic2,(0,140))  #blits it
                    copymx=[] #clears the list
                    copymy=[] #clears the list
                    copyNum=1
                unFilledRect=screen.subsurface(canvasRect).copy()
            except:
                pass
            copymx=[] #clears the list
            copymy=[] #clears the list
            copyNum=1 #number gets to 1
        
    if colorWheel==0:
        screen.blit(colorCirclePic1,(1180,20))
    if colorWheel==1:
        screen.blit(colorCirclePic1,(1180,20))
    if colorWheel==2:
        screen.blit(colorCirclePic2,(1180,20))
    if colorWheel==3:
        screen.blit(colorCirclePic3,(1180,20))
    if colorWheel==4:
        screen.blit(colorCirclePic4,(1180,20))
        
    #select (change) colour
    if mb[0]==1 and colorWheelRect.collidepoint(mx,my):
        
        if (mx-1230)**2+(my-70)**2<=50**2:
            col=screen.get_at((mx,my))
    if mb[0]==1 and colorPaletteRect.collidepoint(mx,my):
        col=screen.get_at((mx,my))
            
    draw.rect(screen,col,(1131,30,35,80))

# load button picture hovered and unhovered
    if loadButtonRect.collidepoint(mx,my):
        screen.blit(loadButtonHovered,(20,20))
    else:
        screen.blit(loadButtonUnHovered,(20,20))
        

    #selected
    if tool=="pencil":
        screen.blit(pencilButtonHovered,(170,30))
    if tool=="eraser":
        screen.blit(eraserButtonHovered,(220,30))
    if tool=="highlighter":
        screen.blit(highlighterButtonHovered,(270,30))
    if tool=="rectangle":
        screen.blit(rectButtonHovered,(389,30))
    if tool=="ellipse":
        screen.blit(ellipseButtonHovered,(539,30))
    if tool=="fountainPen":
        screen.blit(fountainPenButtonHovered,(320,30))
    if tool=="line":
        screen.blit(lineButtonHovered,(539,80))
    if tool=="sprayPaint":
        screen.blit(sprayPaintButtonHovered,(170,80))
    if tool=="brush":
        screen.blit(brushButtonHovered,(270,80))
    if tool=="copyTool":
        screen.blit(copyButtonHovered,(60,105))
    if tool=="colourPicker":
        screen.blit(colourPickerButtonHovered,(220,80))
    if tool=="fillPaint":
        screen.blit(fillPaintButtonHovered,(320,80))
    if tool=="square":
        screen.blit(squareButtonHovered,(389,80))
    if tool=="polygonTool":
        screen.blit(polygonButtonHovered,(461,80))
    if tool=="stamp1":
        screen.blit(stamp1ButtonHovered,(608,30))
    if tool=="stamp2":
        screen.blit(stamp2ButtonHovered,(658,30))
    if tool=="stamp3":
        screen.blit(stamp3ButtonHovered,(708,30))
    if tool=="stamp4":
        screen.blit(stamp4ButtonHovered,(608,80))
    if tool=="stamp5":
        screen.blit(stamp5ButtonHovered,(658,80))
    if tool=="stamp6":
        screen.blit(stamp6ButtonHovered,(708,80))
    if colorWheel==1:
        screen.blit(colorCircle1Hovered,(1290,15))
    if colorWheel==2:
        screen.blit(colorCircle2Hovered,(1290,45))
    if colorWheel==3:
        screen.blit(colorCircle3Hovered,(1290,75))
    if colorWheel==4:
        screen.blit(colorCircle4Hovered,(1290,105))
    if background==1:
        screen.blit(background1Hovered,(777,30))
    if background==2:
        screen.blit(background2Hovered,(777,80))
    if background==3:
        screen.blit(background3Hovered,(887,30))
    if background==4:
        screen.blit(background4Hovered,(887,80))
    if background==5:
        screen.blit(background5Hovered,(997,30))
    if background==6:
        screen.blit(background6Hovered,(997,80))

    #hovering
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilButtonHovered,(170,30))
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserButtonHovered,(220,30))
    if highlighterRect.collidepoint(mx,my):
        screen.blit(highlighterButtonHovered,(270,30))
    if rectangleToolRect.collidepoint(mx,my):
        screen.blit(rectButtonHovered,(389,30))
    if ellipseToolRect.collidepoint(mx,my):
        screen.blit(ellipseButtonHovered,(539,30))
    if fountainPenRect.collidepoint(mx,my):
        screen.blit(fountainPenButtonHovered,(320,30))
    if lineToolRect.collidepoint(mx,my):
        screen.blit(lineButtonHovered,(539,80))
    if sprayPaintToolRect.collidepoint(mx,my):
        screen.blit(sprayPaintButtonHovered,(170,80))
    if brushToolRect.collidepoint(mx,my):
        screen.blit(brushButtonHovered,(270,80))
    if copyRect.collidepoint(mx,my):
        screen.blit(copyButtonHovered,(60,105))
    if colourPickerToolRect.collidepoint(mx,my):
       screen.blit(colourPickerButtonHovered,(220,80)) 
    if fillPaintToolRect.collidepoint(mx,my):
        screen.blit(fillPaintButtonHovered,(320,80))
    if squareToolRect.collidepoint(mx,my):
        screen.blit(squareButtonHovered,(389,80))
    if polygonToolRect.collidepoint(mx,my):
        screen.blit(polygonButtonHovered,(461,80))
    if lineToolRect.collidepoint(mx,my):
        screen.blit(lineButtonHovered,(539,80))
    if backSongRect.collidepoint(mx,my):
        screen.blit(backButtonHovered,(111,779))
    if middleSongRect.collidepoint(mx,my):
        screen.blit(playButtonHovered,(164,780))
    if nextSongRect.collidepoint(mx,my):
        screen.blit(nextButtonHovered,(211,779))
    if musicDownRect.collidepoint(mx,my):
        screen.blit(musicDownButtonHovered,(78,779))
    if musicUpRect.collidepoint(mx,my):
        screen.blit(musicUpButtonHovered,(250,779))          
    if stamp1Rect.collidepoint(mx,my):
        screen.blit(stamp1ButtonHovered,(608,30))
    if stamp2Rect.collidepoint(mx,my):
        screen.blit(stamp2ButtonHovered,(658,30))
    if stamp3Rect.collidepoint(mx,my):
        screen.blit(stamp3ButtonHovered,(708,30))
    if stamp4Rect.collidepoint(mx,my):
        screen.blit(stamp4ButtonHovered,(608,80))
    if stamp5Rect.collidepoint(mx,my):
        screen.blit(stamp5ButtonHovered,(658,80))
    if stamp6Rect.collidepoint(mx,my):
        screen.blit(stamp6ButtonHovered,(708,80))
    if color1PicRect.collidepoint(mx,my):
        screen.blit(colorCircle1Hovered,(1290,15))
    if color2PicRect.collidepoint(mx,my):
        screen.blit(colorCircle2Hovered,(1290,45))
    if color3PicRect.collidepoint(mx,my):
        screen.blit(colorCircle3Hovered,(1290,75))
    if color4PicRect.collidepoint(mx,my):
        screen.blit(colorCircle4Hovered,(1290,105))
    if saveButtonRect.collidepoint(mx,my):
        screen.blit(saveButtonHovered,(82,20))
    else:
        screen.blit(saveButtonUnHovered,(82,20))
    if undoRect.collidepoint(mx,my):
        screen.blit(undoButtonHovered,(15,105))
    else:
        screen.blit(undoButtonUnHovered,(15,105))
    if redoRect.collidepoint(mx,my):
        screen.blit(redoButtonHovered,(105,105))
    else:
        screen.blit(redoButtonUnHovered,(105,105))
    if shapeFill==False:
        screen.blit(shapeFillButtonUnHovered,(439,30))
    elif shapeFill==True:
        screen.blit(shapeFilledButtonHovered,(439,30))

    #MUSIC SONG
    if song==0: #if there is no song selected
        screen.blit(musicPlayer1,(48,683)) #blit the image
        song=4 
    elif song==1: 
        screen.blit(musicPlayer2,(48,683)) #blit image
        mixer.music.load("Music/song1.ogg") #load it
        mixer.music.play() #play song
        tarj=0 #tarj =0 ; make the scrubber set to 0
        song=4
        
    elif song==2:
        screen.blit(musicPlayer3,(48,683)) #blit it
        mixer.music.stop() #stop any song
        mixer.music.load("Music/song2.ogg") #load it
        mixer.music.play() #play it
        tarj=0 #tarj =0 ; make the scrubber set to 0
        song=4
    elif song==3:
        screen.blit(musicPlayer4,(48,683)) #blit it
        mixer.music.stop()
        mixer.music.load("Music/song3.ogg") #load it 
        mixer.music.play() #play song
        tarj=0 #tarj =0 ; make the scrubber set to 0
        song=4
        
    #blits the load and save button pictures
    screen.blit(loadButtonPic,(24,82))
    screen.blit(saveButtonPic,(87,82))


    #TEXT FOR THE PAINT PROJECT (COORDS, NAME, THICKNESS)
    thicknessText=str(thickness)
    thicknessPic=comicFont.render(thicknessText,False,(255,255,255))
    if canvasRect.collidepoint(mx,my):
        mxText=str(mx)
        if 0<=(my-140)<=534:
            myText=str(my-140)
    else:
        mxText="N/A"
        myText="N/A"
    toolText="Tool:"
    thickText="Thickness:"
    XText="X:"
    YText="Y:"
    XPic=comicFont.render(XText,False,(255,255,255))
    mxPic=comicFont.render(mxText,False,(255,255,255))
    myPic=comicFont.render(myText,False,(255,255,255))
    YPic=comicFont.render(YText,False,(255,255,255))
    toolPic=comicFont.render(toolText,False,(255,255,255))
    toolHoveredPic=comicFont.render(toolHovered,False,(255,255,255))
    thickPic=comicFont.render(thickText,False,(255,255,255))
    draw.rect(screen,BLACK,(1250,680,350,100))
    screen.blit(toolPic,(1300,700))
    screen.blit(toolHoveredPic,(1340,700))
    screen.blit(thickPic,(1300,730))
    screen.blit(thicknessPic,(1385,730))
    screen.blit(XPic,(1300,760))
    screen.blit(YPic,(1380,760))
    screen.blit(mxPic,(1320,760))
    screen.blit(myPic,(1400,760))
    omx,omy=mx,my
    
    musicChangerRect=Rect(60,755,210,12)

    if songNumber==1:
        screen.blit(musicPlayer22,(48,683)) #blit image
        if ((60+3*round(mixer.music.get_pos()/1000))-tarj)<=280: #if the position is between
            draw.ellipse(screen,WHITE,(((60+3*round(mixer.music.get_pos()/1000))-tarj),757,10,10)) #draw the ellipse
        else:
            tarj=-999 #put the scrubber out of screen
            draw.ellipse(screen,WHITE,(284,757,10,10)) #put the circle to the first part
            mixer.music.stop() #stop song
    if songNumber==2:
        screen.blit(musicPlayer33,(48,683)) #blit image
        if ((60+3*round(mixer.music.get_pos()/1000))-tarj)<=280: #if the position is between
            draw.ellipse(screen,WHITE,(((60+3*round(mixer.music.get_pos()/1000))-tarj),757,10,10)) #draw the ellipse
        else:
            tarj=-999#put the scrubber out of screen
            draw.ellipse(screen,WHITE,(284,757,10,10)) #put the circle to the first part
            mixer.music.stop() #stop song
    if songNumber==3: #blit image
        screen.blit(musicPlayer44,(48,683))
        if ((60+3*round(mixer.music.get_pos()/1000))-tarj)<280: #if the position is between
            draw.ellipse(screen,WHITE,(((60+3*round(mixer.music.get_pos()/1000))-tarj),757,10,10)) #draw the ellipse
        else:
            tarj=-999#put the scrubber out of screen
            draw.ellipse(screen,WHITE,(284,757,10,10)) #put the circle to the first part
            mixer.music.stop() #stop song
    display.flip()            
quit()
