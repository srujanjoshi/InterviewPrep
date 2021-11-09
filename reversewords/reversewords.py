#Input Format: [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
#Output Format: ['s', 't', 'e', 'a', 'l',' ','p', 'o', 'u', 'n', 'd', ' ','c', 'a', 'k', 'e']
# :O looks like someone is going to steal some pound cake




import unittest


def reverse_words(message):
    #Reverse the entire message in place
    start=0
    end=len(message)-1
    print("Hi")
    while (start<end):
        message[start], message[end]= message[end], message[start]
        start+=1
        end-=1
    # Decode the message by reversing the words
    i=0
    start=0
    end=0
    while(i< len(message)):
        if(message[i]=='' or i == len(message)-1):
            #Begin reversing the words from current start position until i
            print("Hi")
            end=i-1
            while(start<end):
                message[start], message[end]= message[end], message[start]
                start+=1
                end-=1
            start=i+1
    print(message)
        
    pass



reverse_words([ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ])














# # Tests

# class Test(unittest.TestCase):

#     def test_one_word(self):
#         message = list('vault')
#         reverse_words(message)
#         expected = list('vault')
#         self.assertEqual(message, expected)

#     def test_two_words(self):
#         message = list('thief cake')
#         reverse_words(message)
#         expected = list('cake thief')
#         self.assertEqual(message, expected)

#     def test_three_words(self):
#         message = list('one another get')
#         reverse_words(message)
#         expected = list('get another one')
#         self.assertEqual(message, expected)

#     def test_multiple_words_same_length(self):
#         message = list('rat the ate cat the')
#         reverse_words(message)
#         expected = list('the cat ate the rat')
#         self.assertEqual(message, expected)

#     def test_multiple_words_different_lengths(self):
#         message = list('yummy is cake bundt chocolate')
#         reverse_words(message)
#         expected = list('chocolate bundt cake is yummy')
#         self.assertEqual(message, expected)

#     def test_empty_string(self):
#         message = list('')
#         reverse_words(message)
#         expected = list('')
#         self.assertEqual(message, expected)


# unittest.main(verbosity=2)