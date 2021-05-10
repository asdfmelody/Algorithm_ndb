# 큰수의 법칙

import time
#start = time.time()  # 시작 시간 저장

n, m, k= map(int, input().split())
data = list(map(int,input().split()))

start = time.time()  # 시작 시간 저장

data.sort()

result=(data[n-1]*k+data[n-2])*(m//(k+1))+data[n-1]*(m%(k+1))

print(result)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간