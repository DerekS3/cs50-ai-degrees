import unittest
from degrees import *


class TestShortestPath(unittest.TestCase):
    def setUp(self):
        None
        
    def test_shorest_path_1_degree(self):
        load_data('small')
        source = person_id_for_name("Kevin Bacon")
        target = person_id_for_name("Tom Cruise")
        path = shortest_path(source, target)
        expected_result = [('104257', '129')]
        self.assertEqual(path, expected_result)

    def test_shorest_path_none(self):
        load_data('small')
        source = person_id_for_name("Kevin Bacon")
        target = person_id_for_name("Emma Watson")
        path = shortest_path(source, target)
        expected_result = None
        self.assertEqual(path, expected_result)
        


if __name__ == '__main__':
    unittest.main()