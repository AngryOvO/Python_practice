## 선택 정렬 알고리즘

##랜던 모듈 
import random

##2018038025 정하용
## 변수 선언
arr = []
i,k =0,0
mini = 0

## 10개의 16진수 랜덤으로 arr리스트에 할당
for i in range(0,10):
    temp = hex(random.randrange(0,100000))
    arr.append(temp)

##정렬되지 않은 리스트 출력
print(arr)

##선택정렬 알고리즘
for i in range(0,len(arr)-1,1): ## 0부터 배열의 크기 - 1 전까지
    mini = i ## 최솟값을 인덱스 i번째로
    for j in range(i+1, len(arr),1): ## i+1부터 배열의 크기 전까지
        if int(arr[j],16) < int(arr[mini],16): ## 최솟값이 j번째보다 크면
            mini = j ##j가 최솟값의 인덱스
        ##SWAP
        temp = arr[mini]
        arr[mini] = arr[i]
        arr[i] = temp
##정렬된 리스트 출력
print(arr)
        
    
