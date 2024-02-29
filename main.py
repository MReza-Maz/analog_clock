from graphics import *
import math
import time



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
    clockCircle = Circle(Point(width / 2, height / 2), secondLen + 15)
    clockCircle.draw(win)

    for i in range(0, 360, 30):
        sinClockPoint1 = width / 2 + int((secondLen + 10) * math.sin((180 - i) * 2 * math.pi / 360))
        sinClockPoint2 = width / 2 + int((secondLen + 15) * math.sin((180 - i) * 2 * math.pi / 360))
        cosClockPoint1 = height / 2 + int((secondLen + 10) * math.cos((180 - i) * 2 * math.pi / 360))
        cosClockPoint2 = height / 2 + int((secondLen + 15) * math.cos((180 - i) * 2 * math.pi / 360))
        clockLine = Line(Point(sinClockPoint1, cosClockPoint1), Point(sinClockPoint2, cosClockPoint2))
        clockLine.draw(win)


    while True:
        sinSecondPoint = width / 2 + int(secondLen * math.sin((180 - second) * 2 * math.pi / 360))
        cosSecondPoint = height / 2 + int(secondLen * math.cos((180 - second) * 2 * math.pi / 360))
        secondLine = Line(Point(width / 2, height / 2), Point(sinSecondPoint, cosSecondPoint))
        sinMinutePoint = width / 2 + int(minuteLen * math.sin((180 - minute) * 2 * math.pi / 360))
        cosMinutePoint = height / 2 + int(minuteLen * math.cos((180 - minute) * 2 * math.pi / 360))
        minuteLine = Line(Point(width / 2, height / 2), Point(sinMinutePoint, cosMinutePoint))
        sinHourPoint = width / 2 + int(hourLen * math.sin((180 - hour) * 2 * math.pi / 360))
        cosHourPoint = height / 2 + int(hourLen * math.cos((180 - hour) * 2 * math.pi / 360))
        hourLine = Line(Point(width / 2, height / 2), Point(sinHourPoint, cosHourPoint))        
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