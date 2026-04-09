'''def isPalindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))'''

'''haystack = "sadbutsad"
needle = "sad"
index = haystack.find(needle)
print(index)  
print(haystack.find("leeto"))'''


'''def longestCommonPrefix(strs):
    if not strs: return ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for other_str in strs[1:]:
            if i == len(other_str) or other_str[i] != char:
                return strs[0][:i]
    return strs[0]'''


'''def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
        
    for c in count:
        if c != 0:
            return False
    return True'''


def romanToInt(s: str) -> int:
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    return total


# Пример использования:
print(romanToInt("MCMXCIV"))
print(romanToInt("LVIII"))




