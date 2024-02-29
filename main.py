from graphics import *
import math
import time

def getPoint(size, lenth, degree, type):
    if(type == "sin"):
        return(size / 2 + int(lenth * math.sin((180 - degree) * 2 * math.pi / 360)))
    if(type == "cos"):
        return(size / 2 + int(lenth * math.cos((180 - degree) * 2 * math.pi / 360)))

def getLine(x1, y1, x2, y2):
    return(Line(Point(x1,y1), Point(x2, y2)))

def main():
    width = 500
    height = 500
    secondLen = 200
    minuteLen = 175
    hourLen = 150
    second = 0
    minute = 0
    hour = 0

    win = GraphWin("Clock", width, height)
    clockCircle = Circle(Point(width / 2, height / 2), secondLen + 20)
    clockCircle.draw(win)

    for i in range(0, 360, 30):
        clockLine = getLine(getPoint(width, secondLen + 10, i, "sin"), getPoint(height, secondLen + 10, i, "cos"),
                            getPoint(width, secondLen + 20, i, "sin"), getPoint(height, secondLen + 20, i, "cos"))
        clockLine.draw(win)

    while True:
        secondLine = getLine(width / 2, height / 2, getPoint(width, secondLen, second, "sin"), getPoint(height, secondLen, second, "cos"))
        minuteLine = getLine(width / 2, height / 2, getPoint(width, minuteLen, minute, "sin"), getPoint(height, minuteLen, minute, "cos"))
        hourLine = getLine(width / 2, height / 2, getPoint(width, hourLen, hour, "sin"), getPoint(height, hourLen, hour, "cos"))

        secondLine.draw(win)
        minuteLine.draw(win)
        hourLine.draw(win)
        
        time.sleep(1)
        
        second += 6
        if(second == 360):
            second = 0
            minute += 6
        if(minute == 360):
            minute = 0
            hour += 30
        if(hour == 360):
            hour = 0
        
        secondLine.undraw()
        minuteLine.undraw()
        hourLine.undraw()

main()