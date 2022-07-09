# thanks https://cp-algorithms.com/string/prefix-function.html

def stringPrefix(s: str) -> list:
    n = len(s)
    res = [0 for _ in range(n)]
    for i in range(1,n):
        j = res[i-1]
        while j>0 and s[i] != s[j]:
            j = res[j-1]
        # for any value of i, i is the last character of the substring segment s[:i+1]
        # j is effectively the corresponding index to compare with i due to first optimization rule
        if s[i] == s[j]:
            j+=1
        # logs j into res
        res[i] = j
    return res