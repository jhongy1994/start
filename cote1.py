#참석자 리스트 participant와 완주명단 completion을 알 때, 완주하지 못한 한사람을 찾아야 함 (선수이름 중복가능)
#첫번째 해답/ 정확성 OK, 효율성 Bad
# def solution(participant, completion):
#     for comPerson in completion:
#         participant.remove(comPerson)
#     answer = participant[0]
#     return answer
#정확도는 좋으나 속도면에서 나아지지 않음 / 이도저도 아닌 방법인듯
# def solution(participant, completion):
#     setPar = set(participant)
#     setCom = set(completion)
#     if len(setPar)==len(participant):
#         notCom = list(setPar - setCom)
#         answer = notCom[0]
#     else:
#         for comPerson in completion:
#             participant.remove(comPerson)
#         answer = participant[0]
#     return answer
#답안 참고 collection사용
import collections

def solution(participant, completion):
    notCom = collections.Counter(participant) - collections.Counter(completion)
    answer = list(notCom)[0]
    return answer
