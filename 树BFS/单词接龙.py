#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 单词接龙.py 
@time: 2020/7/6 17:06

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        graph = {}
        graph[beginWord] = self.get_neighbours(beginWord, wordList)
        graph[endWord] = self.get_neighbours(endWord, wordList)
        for word in wordList:
            graph[word] = self.get_neighbours(word, wordList)
        distance = {}
        distance[beginWord] = 1
        queue = [beginWord]
        while len(queue) != 0:
            cur_word = queue.pop()
            for neighbour_word in graph[cur_word]:
                if neighbour_word not in distance:
                    distance[neighbour_word] = distance[cur_word] + 1
                    queue.append(neighbour_word)
        if endWord in distance:
            return distance[endWord]
        else:
            return 0

    def get_neighbours(self, word, wordList):
        neighbour = set()
        for idx in range(len(word)):
            left = word[0:idx]
            right = word[idx + 1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                temp_word = left + c + right
                if temp_word in wordList and temp_word != word:
                    neighbour.add(temp_word)

        return neighbour


if __name__ == "__main__":
    s = Solution()
    start = "hit"
    end = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    r = s.ladderLength(start, end, word_list)
    print(r)

    word_list = ["hot", "dot", "dog", "lot", "log"]
    r = s.ladderLength(start, end, word_list)
    print(r)
