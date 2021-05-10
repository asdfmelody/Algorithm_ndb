#거스름돈 문제 - 그리디
#10의 배수인 N원을 거슬러줘야할 동전의 최소 개수 (500, 100, 50, 10)
import time
start = time.time()  # 시작 시간 저장

n= 1260
count=0

for coin in [500,100,50,10]:
  count+=n//coin
  n=n%coin

print(count)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간