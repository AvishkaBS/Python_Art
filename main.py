import turtle #importing turtle function for drawing
import colorsys #importing Colorsys module for HSV coloring

hue=0.0 #defining starting hue value
bg=turtle.Turtle() #Calling turtle function & assigning it to bg variable
bg.getscreen().bgcolor("#352d51") #setting background color

def star(bg,size): #method for drawing a star
    bg.color(mycolor) #set turtle color according to mycolor value
    bg.speed(10000000) #turtle speed
    bg.penup() #penup method to ignore unwanted lines

    if size<=0: #if size value is less than 1 it will stop
        return
    else:
        bg.begin_fill() #if the shape is completed it will fill color
        for i in range(5): #iterating five times
            bg.forward(size/10) #draw the line according to the size value
            bg.left(216) #turn 216 degrees
        bg.end_fill() #stop filling color to the shape
    bg.pendown()

for i in range(0,2000): #Drawing an increasing spiral circle
    bg.speed(1000000000) #Drawing speed
    bg.circle(i,10) #i to iterate circle drawing & the length,second argument is to control the central angle

    mycolor=colorsys.hsv_to_rgb(hue,1,1) #defining my color variable & setting hsv colors

    star(bg,i*0.5) #Calling star method to draw star (multiplying size value by 0.5)

    hue+=0.0025 #increasing hue value by 0.0025 for color changing

turtle.done() #ending turtle method