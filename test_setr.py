import unittest
from src.setr.setr import min as setr_min, max as setr_max, FastRange, MultiRange

class TestFastRange(unittest.TestCase):
    def setUp(self):
        self.fr = FastRange(10, 20)
        
    def test_init(self):
        self.assertTrue(self.fr)

    def test_number_in_fast_range(self):
        self.assertTrue(15 in self.fr)

    def test_numbers_generated_match_normal_range(self):
        fr = (i for i in self.fr)
        for i in range(10, 20):
            self.assertEqual(i, next(fr))
        self.assertRaises(StopIteration, next, fr)
    
    def test_max_of_range(self):
        self.assertEqual(max(self.fr), setr_max(self.fr))

    def test_min_of_range(self):
        self.assertEqual(max(self.fr), setr_max(self.fr))

class TestMultiRange(unittest.TestCase):
    def setUp(self):
        self.mr = MultiRange()
        self.mr.add_range(FastRange(10,20))
        self.mr.add_range(FastRange(15, 30))
        self.mr.add_range(FastRange(1000, 2000))

    def test_init(self):
        self.assertTrue(self.mr)
        
    def test_number_in(self):
        self.assertTrue(12 in self.mr)
    
    def test_number_in_on_range_overlap(self):
        self.assertTrue(16 in self.mr)
        
    def test_number_outside_of_range(self):
        self.assertFalse(55 in self.mr)

    def test_count_of_range(self):
        self.assertEqual(self.mr.count_in(16), 2)

    def test_max_of_range(self):
        self.assertEqual(setr_max(self.mr), 1999)

    def test_min_of_range(self):
        self.assertEqual(setr_min(self.mr), 10)

    def test_safely_flatten(self):
        new_mr = self.mr.safely_flatten()
        self.assertEqual(len(new_mr.ranges), 2)
        self.assertEqual(len(self.mr.ranges), 3)
        self.assertEqual(setr_min(new_mr), setr_min(self.mr))
        self.assertEqual(setr_max(new_mr), setr_max(self.mr))
    
    def test_flatten(self):
        self.mr.flatten()
        self.assertEqual(len(self.mr.ranges), 2)
