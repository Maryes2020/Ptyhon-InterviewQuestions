def palindrome(s):
    	temp = []
	res1 = []
	for i in range(len(s)):
		j = 1
		while j < min(len(s[:i+1]),len(s[i:]) )and s[i+j] == s[i-j]:
			if temp == []:
				temp.append(s[i])
			temp.insert(0, s[i-j])
			temp.append(s[i+j])	
			j+=1
		res1, temp = max(temp,res1,key=len) , []
	temp = []
	res2 = []
	for i in range(len(s)):	
		j = 1
		while j < min(len(s[:i+1]),len(s[i:]) ) and s[i] == s[i+1] and s[i-j] == s[i+1+j]:
			if temp == []:
				temp.append(s[i])
				temp.append(s[i])
			temp.insert(0, s[i-j])
			temp.append(s[i+1+j])	
			j+=1
		res2, temp = max(temp,res2) , []
	return "".join(max(res1,res2,key=len))
s = 'aabcdcb'
print(palindrome(s))


# Çözüm-1
def longestpalindrom(text):
    result = ""
    for i in range(len(text)):
        for j in range(len(text),i,-1):
            if (text[i:j] == text[i:j][::-1]) and len(result) < len(text[i:j]):
                result = text[i:j]
    return result

# Çözüm-2
def longestpalindrom2(text):
    return max([text[i:j] for i in range(len(text)) for j in range(len(text),i,-1) if (text[i:j] == text[i:j][::-1])], key = len)