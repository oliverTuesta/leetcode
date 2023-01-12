# https://leetcode.com/problems/multiply-strings/
# Difficulty: Medium 

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mult = [] 
        for i in range (len(num1) - 1, -1, -1):
            m = "0" * (len(num1) + len(num2))
            x = i + len(num2)
            carry = 0
            for j in range (len(num2) - 1, -1, -1):
                n = int(num1[i]) * int(num2[j]) + carry
                carry = int(n / 10)
                if j > 0 and n >= 10:
                    n = n % 10
                    m = m[:x] + str(n) + m[x+1:]
                m = m[:x] + str(n) + m[x+1:]
                if j == 0 and carry > 0:
                    m = m[1:]
                x -= 1
            mult.append(m)
        ans = ""
        carry = 0
        for j in range (len(num1) + len(num2) - 1, -1, -1):
            sum = 0
            for i in range (0, len(num1)):
                sum += int(mult[i][j])
            sum += carry
            carry = int(sum / 10)
            if j > 0:
                sum = sum % 10
            ans = str(sum) + ans

        i = 0
        while (i < len(ans) and ans[i] == "0"):
            ans = ans[1:]
        if ans == "":
            return "0"
        return ans

s = Solution()
print(s.multiply("9133", "923142134"))
