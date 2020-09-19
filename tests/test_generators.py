# import pytest
import unittest

from counters.numberators import add_one

class TestCounters(unittest.TestCase):

	def test_add_one(self):
		self.assertEqual(add_one(1), 2)
		
if __name__ == '__main__':
	unittest.main()
