# Time Complexity: O()
# Space Complexity: O()

def isPalindrome(s):
    start = 0
    end = len(s)-1

    # aba | abba
    while start <= end:

        while start < end and not isalpha(s[start]):
            start += 1
        while start < end and not isalpha(s[end]):
            end -= 1

        if s[start].lower() != s[end].lower():
            return False
        
        start, end = start + 1, end -1
    
    return True

def isalpha(c):
    return ((ord("0") <= ord(c) <= ord("9")) or
            (ord("a")<= ord(c) <= ord("z")) or
            (ord("A")<= ord(c) <= ord("Z")))

input = "A man, a plan, a canal: Panama"
# input = "abac"
output = isPalindrome(input)
print(output)