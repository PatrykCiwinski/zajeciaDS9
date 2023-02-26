import unittest
from ut_mod_data import get_data


class NameTest(unittest.TestCase):
    def test_First_last(self):
        data = get_data('Patryk', 'Ciwiński')
        self.assertEqual(data, 'Patryk Ciwiński')