##turtle 모듈 , 랜덤 모듈 가져옴
import turtle 
import random

## 변수 선언구간
myTurtle, tX, tY, tColor, tSize, tShape = [None] * 6
##거북이 리스트 선언
playerTurtles = []
swidth, sheight = 500, 500

if __name__ == "__main__" :
    turtle.title('거북 리스트 활용(정렬)')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
## 2018038025 정하용
    ## 5번에 걸쳐서 5개의 거북이의 랜덤 위치 랜덤 크기 랜덤 색깔 설정
    for i in range(0, 5) :
        myTurtle = turtle.Turtle('turtle')
        tX = random.randrange(-swidth / 2, swidth / 2)
        tY = random.randrange(-sheight / 2, sheight / 2)
        r = random.random(); g = random.random(); b = random.random()
        tSize = random.randrange(1, 10)
        ## 설정된 거북이들의 값들을 리스트에 할당
        playerTurtles.append([myTurtle, tX, tY, tSize, r, g, b])
    ## 리스트중에 키값을 거북이의 크기를 기준으로 정렬
    sortedTurtles = sorted(playerTurtles, key = lambda turtles : turtles[3])

    ## 정렬된 거북이 리스트 실행
    for index, tList in enumerate(sortedTurtles[0:]):
        myTurtle = tList[0]
        myTurtle.color((tList[4], tList[5], tList[6]))
        myTurtle.pencolor((tList[4], tList[5], tList[6]))
        myTurtle.turtlesize(tList[3])
        ## 거북이 랜덤한 각도로 회전
        myTurtle.left(random.randrange(0,360))
        myTurtle.penup()
        if index == 0:
            myTurtle.goto(tList[1], tList[2])
            continue
        myTurtle.goto(sortedTurtles[index-1][1], sortedTurtles[index-1][2])
        ## 선을 긋고
        myTurtle.pendown()
        ## 거북이 이동
        myTurtle.goto(tList[1], tList[2])

turtle.done()## 거북이 종료
