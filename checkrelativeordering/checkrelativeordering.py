import unittest

def is_first_come_first_served(list_a, list_b, combined_list): 
    list_a_index=0
    list_b_index=0
    combined_list_index=0
    while(combined_list_index<len(combined_list)):
        if(list_a_index <len(list_a)):
            if(list_a[list_a_index]==combined_list[combined_list_index]):
                list_a_index+=1
                combined_list_index+=1
                continue
        if(list_b_index<len(list_b)):
            if(list_b[list_b_index]==combined_list[combined_list_index]):
                list_b_index+=1
                combined_list_index+=1
                continue
        return False
    if(list_a_index!=len(list_a) or list_b_index!=len(list_b)):
        return False
    return True 

# print(is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))

# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)