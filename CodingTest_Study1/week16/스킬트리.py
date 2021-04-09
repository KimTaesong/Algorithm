def solution(skill: str, skill_trees: list) -> int:
    cnt = 0
    for skill_tree in skill_trees:  # iterator 활용
        idx = 0  # skill의 idx
        flag = True  # 주어진 skill 순서를 만족하는지 체크하는 플래그
        print(skill_tree)
        # skill_tree의 각 문자열과 skill의 idx값을 비교, 같으면 idx를 추가 해줌.
        for i in range(len(skill_tree)):
            if idx < len(skill) and skill_tree[i] == skill[idx]:
                print(skill[idx])
                idx += 1
                continue

            if skill.find(skill_tree[i]) > idx:  # 다른 경우, 주어진 스킬트리의 idx값을
                print(skill.find(skill_tree[i]), idx)
                flag = False
                break

        if flag == True:
            cnt += 1

    return cnt


print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))
