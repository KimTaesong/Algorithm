def solution(w, h):

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    return w * h - (w+h-gcd(w, h))
