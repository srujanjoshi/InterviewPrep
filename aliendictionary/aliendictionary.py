from typing import List


class Solution:
    def alienOrder1(self, words: List[str]) -> str:
        
        if(len(words)==1):
            return str(set(words[0]))
        
        order = {}
        #First construct the graph, by iterating over each pair of words: 

        #Not sure if you can just iterate over each consequtive pair of words,
        for i in range(len(words)-1):
            for j in range(i+1, len(words)): 
                first_word = words[i]
                second_word = words[j]
                
                left, right = 0,0
                while(left<len(first_word) and right<len(second_word)):
                    if(first_word[left]!= second_word[right]):
                        #We have found the first letter position at which they differ
                        #This must mean that the letter in the first word comes BEFORE the letter in the second word
                        if (first_word[left] in order):
                            order[first_word[left]].add(second_word[right])
                        else:
                            order[first_word[left]]= {second_word[right]}
                        break
                    left+=1
                    right+=1 
                
                if(first_word[left-1]==second_word[right-1]):
                    #If we have not yet found the letter position at which they differ, this must mean that first_word is a prefix of second_word
                    #If the first min(len(first_word),len(second_word)) characters are the same, then a
                    #valid ordering exists only if len(first_word)<=len(second_word) (= because there might be duplicates listed consecutively which is fine)
                    if(len(first_word)> len(second_word)):
                        return ""
        

        return order


    def alienOrder2(self, words: List[str]) -> str:
        
        if(len(words)==1):
            return 

        #First construct the graph, by iterating over each pair of words: 
        order = {}

        #Not sure if you can just iterate over each consequtive pair of words,

        i,j = 0,1 
        while(i< len(words)-1):
            first_word = words[i]
            second_word = words[j]
            
            left, right = 0,0
            while(left<len(first_word) and right<len(second_word)):
                if(first_word[left]!= second_word[right]):
                    #We have found the first letter position at which they differ
                    #This must mean that the letter in the first word comes BEFORE the letter in the second word
                    if (first_word[left] in order):
                        order[first_word[left]].add(second_word[right])
                    else:
                        order[first_word[left]]= {second_word[right]}
                    break
                left+=1
                right+=1 
            
            if(first_word[left-1]==second_word[right-1]):
                #If we have not yet found the letter position at which they differ, this must mean that first_word is a prefix of second_word
                #If the first min(len(first_word),len(second_word)) characters are the same, then a
                #valid ordering exists only if len(first_word)<=len(second_word) (= because there might be duplicates listed consecutively which is fine)
                if(len(first_word)> len(second_word)):
                    return ""
            i+=1
            j+=1
        

        return order




print(Solution().alienOrder2(["wrt","wrf","er","ett","rftt"]))
        