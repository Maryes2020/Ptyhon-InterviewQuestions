class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = res = ""
        if strs == []:
	        return ""
        for i in range(len(min(strs,key=len))):
            x = strs[0][i]
            for j in strs:
                if j[i]!=x:
                    return res
                else:
                    temp = j[i]
            res += temp
        return res

# çözüm-1
def longestCommonPrefix1(strs):
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        short = min(strs,key = len)
        result = ""
        index = 0
        while index < len(short):
            for i in range(len(strs)):
                if strs[i][index] != short[index]:
                    return result
            result += short[index]
            index += 1
        return result


# çözüm-2
def longestCommonPrefix2(strs):
    result = ""
    index = 0
    try:
        short = min(strs,key = len)
        result = ""
        i = 0
        while i < len(short):
            for item in strs:
                if item[i] != short[i]:
                    return result
            result += short[i]
            i += 1
    except:
        return result
    return result

# çözüm-3
def longestCommonPrefix3(strs):
    if len(strs) < 2:
        return strs[0] if strs else ""
    lst = [i for i in range(len(min(strs,key = len))) for j in range(len(strs)) if strs[j][i] != strs[0][i]]
    return strs[0][:min(lst)] if lst else min(strs,key = len)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = list(zip(*strs))
        b = ''
        for i in a:
            if len(set(i)) == 1:
                b+=i[0]
            else:
                return b
        return b

words = ["flower","flow","flight"]
def f(words,criteria=sorted(words, key=len)[0]):
  if len(criteria)==0:
    return " "
  elif all([ word.startswith(criteria) for word in words]):
    return criteria
  else:
    return f(words, criteria = criteria[:-1])
print(f(words))