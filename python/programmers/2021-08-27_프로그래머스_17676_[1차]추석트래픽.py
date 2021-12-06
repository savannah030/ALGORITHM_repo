# 초당 최대 처리량: 요청의 응답 "완료 여부에 관계없이" 임의 시간"부터" 1초(=1,000밀리초)간 처리하는 요청의 최대 개수
# 그 문자열 2016-09-15 03:10:33.020 0.011s은 "2016년 9월 15일 오전 3시 10분 33.010초"부터 "2016년 9월 15일 오전 3시 10분 33.020초"까지 "0.011초" 동안 처리된 요청을 의미한다. 
# #########(처리시간은 시작시간과 끝시간을 포함) ########### 문제를 잘읽자
# 16분 알고리즘 구상
# (lines 돌면서 각각 line 시작점과 끝점 비교하여 "처리량 바뀌는 지점만 추가") ###### 노노노 '초당 최대 처리량' 제대로 읽지않아서 알고리즘 잘못생각했었음
# 19분 시작점을 어떻게 구해야할지 고민....
# 36분 startIdx 구함
# 42분 이것저것 정리
# 50분 answer 못구하겠음 문제를 제대로 안봐서 생긴 문제(# 초당확인하면 되잖아......... 문제를 잘읽자)
# +11분 해보려고 했는데 머리 잘 안돌아감...(이중 for문 머리안돌아갔음) 꼭 나중에 다시풀기!!! 성공

# 실수도 2진수로 처리하기 때문에 실수 정보를 표현하는 데에 한계가 있음 따라서 round 함수 씀
# https://ysyblog.tistory.com/162

def solution(lines):

    # lines[0]을 기준으로 보정
    S1,S2,T = lines[0][11:19], float("0"+lines[0][19:23]),float(lines[0][24:-1]) # # S1= 20:59:57 S2= 0.421(실수) T= 0.351
    S1 = S1.split(":")
    endIdx = int(S1[0])*3600+int(S1[1])*60+int(S1[2])+S2
    startIdx = round(endIdx-T+0.001,3)

    # 전처리
    times = []
    for line in lines: 
        S1,S2,T = line[11:19], float("0"+line[19:23]),float(line[24:-1]) # # S1= 20:59:57 S2= 0.421(실수) T= 0.351
        S1 = S1.split(":")
        endTime = int(S1[0])*3600+int(S1[1])*60+int(S1[2])+S2
        startTime = round(endTime-T+0.001,3)
        times.append([round(startTime-startIdx,3),round(endTime-startIdx,3)])
 
    answer = 0
    for i in range(len(times)):
        count = 1 # 자기자신 포함
        for j in range(i+1,len(times)):
            if times[i][1]<=times[j][1]<=(times[i][1]+0.999): #j의 끝나는 시간이 트래픽 범위안에 있으면
                count += 1
            elif times[j][0]<=times[i][1] and times[j][1]>=times[i][1]: #j의 요청시간이 트래픽 범위안에 있으면
                count += 1 
            elif times[i][1]<=times[j][0]<=(times[i][1]+0.999): #j의 시작시간이 트래픽 범위안에 있으면
                count += 1 

        if answer<count:
            answer = count

    return answer     
        
      


# 응답완료시간 S를 기준으로 오름차순 정렬
print(solution([ # 2
    "2016-09-15 01:00:04.001 2.0s", 
    "2016-09-15 01:00:07.000 2s"
]))

print(solution([ # 7
"2016-09-15 20:59:57.421 0.351s", # 응답완료시간S, 처리시간T(최대3초)
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
