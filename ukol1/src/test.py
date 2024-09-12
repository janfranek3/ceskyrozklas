import unittest
from mylib import *

class TestUkol1(unittest.TestCase):

    table1 = [['id1', 'name1',1,2], ['id1', '',1,2], ['id1', '',1,2], ['id1', 'name2',1,2]]
    table2 = [['id1', '',1,2], ['id2', '',1,2]]
    table3 = [['id1', '',1,2], ['id2', '',1,2], ['id2', '',1,2]]

    def test_table1(self):
        self.assertEqual(rowIndicesToRemove(self.table1), [2,3])

    def test_table2(self):
        self.assertEqual(rowIndicesToRemove(self.table2), [])

    def test_table3(self):
        self.assertEqual(rowIndicesToRemove(self.table3), [3])



if __name__ == '__main__':
    unittest.main()
