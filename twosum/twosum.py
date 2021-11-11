import unittest


def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    length_set=set()
    for first_movie_length in movie_lengths:
        if (flight_length-first_movie_length) in length_set:
            return True
        length_set.add(first_movie_length)
    
    return False





    # def twoSum(self, movie_lengths, flight_length):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     dict={}
    #     for i in range(len(movie_lengths)):
    #         first_movie_length= movie_lengths[i]
    #         if(flight_length-first_movie_length) in dict:
    #             return [i,dict[flight_length-first_movie_length]]
    #         dict[first_movie_length]=i

    #     return []

# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_multiple_movies_shorter_than_flight(self):
        result = can_two_movies_fill_flight([5, 6, 7, 8], 9)
        self.assertFalse(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)