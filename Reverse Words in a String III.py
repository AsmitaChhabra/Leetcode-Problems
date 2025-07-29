class Solution(object):
    def reverseWords(self, s):
        words = s.split(" ")
        reversed_words = [] 
        for word in words:
            reversed_word = word[::-1]
            reversed_words.append(reversed_word)
        return " ".join(reversed_words)

#link : https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
