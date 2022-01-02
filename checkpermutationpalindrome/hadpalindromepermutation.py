import unittest


def has_palindrome_permutation(the_string):
    
    counts={}
    # Check if any permutation of the input is a palindrome
    for char in the_string:
        if char in counts: 
            counts[char]+=1
        else:
            counts[char]=1
    num_odd=0
    for k in counts:
        if counts[k] % 2== 1:
            num_odd+=1
            if(num_odd>1):
                return False
    return True


















# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)