import unittest

from challenge.create_vehicle import *

class TestBOM(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bom = [
        {
            'factory': 1,
            'part_name': 'wheels',
            'quantity': 6,
        },
        {
            'factory': 2,
            'part_name': 'space_ship_body',
            'quantity': 1,
        },
        {
            'factory': 3,
            'part_name': 'rockets',
            'quantity': 4,
        },
        {
            'factory': 1,
            'part_name': 'doors',
            'quantity': 3,
        },
    ]

    def test_bom_doesnt_return_zero_objects(self):
    	result = build_vehicle(self.bom)
    	assert result is []