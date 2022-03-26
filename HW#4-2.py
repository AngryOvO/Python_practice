import operator

## 튜플을 저장한 리스트 선언
trainTL = [('토마스',5),('헨리',8), ('에드워드',9),('에밀리',5),('토마스',4),('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
## 딕셔너리와 리스트 선언
traindic,trainlist = {},[]
##2018038025 정하용

tuptup = None
##전체랭크와 현재랭크 1로 초기화해서 선언
totalRank, currentRank = 1,1

## 입력값을 딕셔너리로
for tuptup in trainTL:
    tName = tuptup[0]
    tweight = tuptup[1]
    ## 딕셔너리에 이름이 같으면 수송량만 더해준다 
    if tName in traindic:
        traindic[tName] += tweight
    else :
        traindic[tName] = tweight
        ## 기차 수송량 출력
print('기차 수송량 목록 ==> ', trainTL)
print('-----------------')
## 정렬
trainlist = sorted(traindic.items(), key = operator.itemgetter(1),reverse = True)
print('기차\t총 수송량\t순위')
print('---------------------')
##첫 번째 기차는 1위이므로 먼저 출력
print(trainlist[0][0], '\t', trainlist[0][1], '\t', currentRank)
## 두번째 기차부터 출력
for i in range(1,len(trainlist)):
    totalRank += 1
    ## 현재 수송량과 다음 수송량이 같으면 패스
    if trainlist[i][1] == trainlist[i-1][1]:
        pass
    else:
        currentRank = totalRank
    print(trainlist[i][0], '\t', trainlist[i][1], '\t', currentRank)
    
