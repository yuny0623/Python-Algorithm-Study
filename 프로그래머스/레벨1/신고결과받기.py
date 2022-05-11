'''
0750 ~ 0938 
문제 링크: 
https://programmers.co.kr/learn/courses/30/lessons/92334

도움받은 링크: 
https://dongdongfather.tistory.com/69

팁: 
defaultdict 를 알면 좀 많이 빨리 풀 수 있음. 
'''

from collections import defaultdict 
def solution(id_list, report, k):
    #각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
    answer = [0] * len(id_list)
    report = set(report)
    
    reported_count = defaultdict(int) # 신고된 횟수 
    do_report_and_be_report = defaultdict(set) # 누가 누구를 신고 했는지  
    kill = [] # 정지된 사람 
    for row in report:
        do_report, be_report = row.split()
        reported_count[be_report] += 1
        do_report_and_be_report[do_report].add(be_report)
        
        if reported_count[be_report] == k:
            kill.append(be_report)
    for k in kill:
        for i in range(len(id_list)):
            if k in do_report_and_be_report[id_list[i]]:
                answer[i] += 1
        
    return answer