from unittest import TestCase
import unittest
from testing.city_function import city_function_demo

class City_Test(TestCase):

    def city_test_fn(self):
        formatted_name = city_function_demo("santiago","chile",4000)
        self.assertEqual(formatted_name,"chille santiago 5000")
if __name__=="__main__":
    unittest.main()