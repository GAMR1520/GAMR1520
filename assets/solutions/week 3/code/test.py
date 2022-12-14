"Tests for the core 2048 functions"

import unittest

import core

class TestStackLeft(unittest.TestCase):

    def test_empty(self):
        "An empty row is unaffected by a move"
        result = core.stack_left([None, None, None, None])
        self.assertEqual(result, [None, None, None, None])

    def test_one_value(self):
        "A single non-None tile should be moved to the left"
        result = core.stack_left([None, None, 2, None])
        self.assertEqual(result, [2, None,  None, None])

    def test_two_values(self):
        "Two non-None tiles should be moved to the left and retain their order"
        result = core.stack_left([None, 2, None, 4])
        self.assertEqual(result, [2, 4,  None, None])

    def test_three_values(self):
        "Three non-None tiles should be moved to the left and retain their order"
        result = core.stack_left([None, 2, 4, 2])
        self.assertEqual(result, [2, 4, 2, None])

    def test_four_values(self):
        "All non-None tiles should not move"
        result = core.stack_left([4, 2, 4, 2])
        self.assertEqual(result, [4, 2, 4, 2])


class TestMergeLeft(unittest.TestCase):

    def test_empty(self):
        "An empty row is unaffected by a merge"
        result = core.merge_left([None, None, None, None])
        self.assertEqual(result, [None, None, None, None])

    def test_all_different(self):
        "Different values are unaffected by a merge"
        result = core.merge_left([2, 4, 8, 16])
        self.assertEqual(result, [2, 4, 8, 16])
        
    def test_one_value(self):
        "An single value is unaffected by a merge"
        result = core.merge_left([2, None, None, None])
        self.assertEqual(result, [2, None, None, None])

    def test_one_pair(self):
        "A single pair is simple"
        result = core.merge_left([2, 2, None, None])
        self.assertEqual(result, [4, None,  None, None])

    def test_value_before_pair(self):
        "Simple merge with an additional tile to the left"
        result = core.merge_left([4, 2, 2, None])
        self.assertEqual(result, [4, 4, None, None])

    def test_value_after_pair(self):
        "Simple merge with an additional tile to the right"
        result = core.merge_left([2, 2, 2, None])
        self.assertEqual(result, [4, None, 2, None])

    def test_two_pairs(self):
        "Two pairs leaves a gap"
        result = core.merge_left([2, 2, 2, 2])
        self.assertEqual(result, [4, None, 4, None])

    def test_larger_numbers(self):
        "A large pair with two tiles to the left"
        result = core.merge_left([64, 128, 256, 256])
        self.assertEqual(result, [64, 128, 512, None])


class TestMove(unittest.TestCase):

    def test_empty(self):
        "An empty grid is unaffected by a merge"
        input = [[None, None, None, None], 
                 [None, None, None, None], 
                 [None, None, None, None], 
                 [None, None, None, None]]

        self.assertEqual(core.move_left(input), input)
        self.assertEqual(core.move_right(input), input)

    def test_value_after_pair(self):
        "The additional tile on each row should be stacked into the merged pair"
        input = [[None, 4,    4,  8], 
                 [2,    None, 2,  2], 
                 [None, 2,    2,  2], 
                 [16,   None, 16, 4]]

        left = [[8,  8, None, None], 
                [4,  2, None, None], 
                [4,  2, None, None], 
                [32, 4, None, None]]

        right = [[None, None, 8,  8], 
                 [None, None, 2,  4], 
                 [None, None, 2,  4], 
                 [None, None, 32, 4]]

        self.assertEqual(core.move_left(input), left)
        self.assertEqual(core.move_right(input), right)

    def test_all_twos(self):
        "Two pairs are both merged and stacked"
        input = [[2, 2, 2, 2], 
                 [2, 2, 2, 2], 
                 [2, 2, 2, 2], 
                 [2, 2, 2, 2]]

        left = [[4, 4, None, None],
                [4, 4, None, None],
                [4, 4, None, None],
                [4, 4, None, None]]

        right = [[None, None, 4, 4], 
                 [None, None, 4, 4], 
                 [None, None, 4, 4], 
                 [None, None, 4, 4]]

        self.assertEqual(core.move_left(input), left)
        self.assertEqual(core.move_right(input), right)

class TestReverse(unittest.TestCase):

    def test(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, 16]]
        output = [[ 4,  3,  2,  1], 
                  [ 8,  7,  6,  5], 
                  [12, 11, 10,  9], 
                  [16, 15, 14, 13]]
        self.assertEqual(core.reverse(input), output)

class TestTranspose(unittest.TestCase):

    def test(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, 16]]
        output = [[ 1,  5,  9, 13], 
                  [ 2,  6, 10, 14], 
                  [ 3,  7, 11, 15], 
                  [ 4,  8, 12, 16]]
        self.assertEqual(core.transpose(input), output)

class TestHasGaps(unittest.TestCase):

    def test_no_gaps(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, 16]]
        self.assertFalse(core.has_gaps(input))

    def test_one_gap(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, None]]
        self.assertTrue(core.has_gaps(input))

class TestVerticalMerges(unittest.TestCase):

    def test_no_merges(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, 16]]
        self.assertFalse(core.has_vertical_merges(input))

    def test_one_merge(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 10, 15, 16]]
        self.assertTrue(core.has_vertical_merges(input))

class TestHorizontalMerges(unittest.TestCase):

    def test_no_merges(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 11, 12], 
                  [13, 14, 15, 16]]
        self.assertFalse(core.has_horizontal_merges(input))

    def test_one_merge(self):
        input  = [[ 1,  2,  3,  4], 
                  [ 5,  6,  7,  8], 
                  [ 9, 10, 10, 12], 
                  [13, 14, 15, 16]]
        self.assertTrue(core.has_horizontal_merges(input))

class TestHorizontalPoints(unittest.TestCase):

    def test_no_points(self):
        input  = [[None, None, None, None], 
                  [   2,    4,    8,    4], 
                  [   2,    4,    8,    4], 
                  [   2,    4,    8,    4]]
        self.assertEqual(core.horizontal_points(input), 0)

    def test_some_points(self):
        input  = [[None, None, None, None], 
                  [   2,    2,    8,    4], 
                  [   2,    4,    8,    8], 
                  [   2,    4,    8,    4]]
        self.assertEqual(core.horizontal_points(input), 20)

class TestVerticalPoints(unittest.TestCase):

    def test_no_points(self):
        input  = [[None, None, None, None], 
                  [   2, None,    8,    4], 
                  [   4,    8,    4,    2], 
                  [   2,    4,    8,    4]]
        self.assertEqual(core.vertical_points(input), 0)

    def test_some_points(self):
        input  = [[None, None, None, None], 
                  [   2,    2,    8,    4], 
                  [   2,    4,    8,    8], 
                  [   2,    4,    8,    4]]
        self.assertEqual(core.vertical_points(input), 28)



if __name__ == '__main__':
    unittest.main()