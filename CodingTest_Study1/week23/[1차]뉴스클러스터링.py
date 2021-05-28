def solution(str1, str2):
    s1 = [str1[i:i+2].lower()
          for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower()
          for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    or_set = sum(max(s1.count(i), s2.count(i)) for i in set(s1) | set(s2))
    and_set = sum(min(s1.count(i), s2.count(i)) for i in set(s1) & set(s2))

    if or_set == 0:
        return 65536
    return int((and_set / or_set)*65536)
