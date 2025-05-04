# Diana Maldonado
# April 22, 2025
# Homework-Lab08

import unittest
from string_calculator import StringCalculator  # Assuming the class is in this file

class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = StringCalculator()
    
    #1.
    ##Handles empty input strings
    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)
    
    #2.
    def test_single_number(self):
        self.assertEqual(self.calc.add("5"), 5)
    
    #3.
    ##Converts the numbers to integers and sum them up
    def test_two_numbers_comma_delimited(self):
        self.assertEqual(self.calc.add("2,3"), 5)
    
    #4.
    ##Splits the input string into numbers
    def test_multiple_numbers_comma_delimited(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)
    '''
    #5.
    def test_spaces_between_numbers(self):
        self.assertEqual(self.calc.add(" 1 , 2 "), 3)
    '''
    #6.
    ##It ignores numbers greater than 1000
    def test_ignores_numbers_greater_than_1000(self):
        self.assertEqual(self.calc.add("2,1001"), 2)

    #7.
    ##It ignores numbers greater than 1000
    def test_only_large_numbers(self):
        self.assertEqual(self.calc.add("1001,2000,3000"), 0)

    #8.
    ##It raises a ValueError exception if the input contains negative numbers.
    def test_negative_number_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3,-4")
        self.assertIn("Negatives not allowed: -2, -4", str(context.exception))

    #9.
    ##If non-numeric values are included in the string, it handles them and raises ValueError
    def test_negative_and_non_numeric(self):
        with self.assertRaises(ValueError):
            self.calc.add("-1,x,-5")

    #10.
    def test_non_numeric_ignored(self):
        self.assertEqual(self.calc.add("2,x,3"), 5)
    '''
    #11.
    ##Determines the delimiter(s) 
    def test_newline_as_delimiter(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)
    '''

    #12.
     ##It handles custom delimiters...that are specified using the format //[delimiter]\n.
    def test_custom_single_char_delimiter(self):
        self.assertEqual(self.calc.add("//[;]\n1;2"), 3)

    #13.
    ##It handles different types of delimiters...that are specified using the format //[delimiter]\n.
    def test_custom_delimiter_with_newline(self):
        self.assertEqual(self.calc.add("//[*]\n1*2\n3"), 6)
    
    #14.
    def test_custom_delimiter_special_char(self):
        self.assertEqual(self.calc.add("//[$]\n1$2$3"), 6)

    #15.
    def test_custom_multi_char_delimiter(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)
    '''
    #16.
    def test_multiple_custom_delimiters(self):
        # If implemented: support for multiple delimiters like //[*][%]
        # This test might fail if your current code doesn’t support it yet.
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)
    '''    
    #17. 
    def test_delimiter_same_as_digit(self):
        self.assertEqual(self.calc.add("//[1]\n211312"), 7)  # 2 + 3 + 2

    #18. 
    def test_mixed_delimiters_and_large_numbers(self):
        self.assertEqual(self.calc.add("//[&]\n1000&1001&2"), 1002)


if __name__ == '__main__':
    unittest.main()


##Usage:
#SC=StringCalculator()
#print(SC.add('2,3,4'))   #-> should pring 9
#print(SC.add('//[*]\n1*9'))  #->delimiter is *, should print 10