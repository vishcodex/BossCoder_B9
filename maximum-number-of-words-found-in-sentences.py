# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

# You are given an array of strings sentences, where each sentences[i] represents a single sentence.

# Return the maximum number of words that appear in a single sentence.


from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_list = []
        for i in sentences:
            max_list.append(len(i.split()))
        return max(max_list)

            

if __name__ == '__main__':
    sentences_array = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    ob = Solution()
    res = ob.mostWordsFound(sentences_array)
    print(res)