
class Solution(object):
    def interpret(self, command):
        result = ""
        i = 0 
        while i < len(command):
            if command[i] == "G":
                result += "G"
                i += 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                result += "al"
                i += 4
        return result


"""
Problem: Goal Parser Interpretation
Link: https://leetcode.com/problems/goal-parser-interpretation/
Solution by: Asmita Chhabra — [LeetCode Discuss](https://leetcode.com/problems/goal-parser-interpretation/solutions/7010396/goal-parser-by-asmitachhabra-s6cn/)
Difficulty: Easy

-------------------------------
Intuition:
The command string contains a combination of "G", "()", and "(al)".
Each part translates as:
- "G"   → "G"
- "()"  → "o"
- "(al)"→ "al"

Instead of analyzing character-by-character, we scan the string with an index pointer and match substrings directly.

-------------------------------
Approach:
- Use a while loop with index `i`
- If `command[i] == 'G'`: append 'G' to result, move i by 1
- If `command[i:i+2] == '()'`: append 'o', move i by 2
- If `command[i:i+4] == '(al)'`: append 'al', move i by 4

-------------------------------
 Time Complexity: O(n) — where n is the length of the input
 Space Complexity: O(n) — to store the resulting string
"""

