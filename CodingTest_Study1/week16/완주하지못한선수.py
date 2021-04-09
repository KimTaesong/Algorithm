def solution(participant: list, completion: list) -> str:
    answer = ''
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        if i == len(completion) - 1:
            # print(i)
            answer = participant[i+1]
    return answer


participant = [
    ["leo", "kiki", "eden"],
    ["marina", "josipa", "nikola", "vinko", "filipa"],
    ["mislav", "stanko", "mislav", "ana"]]
completion = [
    ["eden", "kiki"],
    ["josipa", "filipa", "marina", "nikola"],
    ["stanko", "ana", "mislav"]]

for i in range(3):
    print(solution(participant[i], completion[i]))
