import unittest
from primetest import is_prime

class Tests(unittest.TestCase):
  def test1(self):
    self.assertFalse(is_prime(1))

  def test2(self):
    self.assertFalse(is_prime(2))

  def test8(self):
    self.assertFalse(is_prime(8))

  def test11(self):
    self.assertFalse(is_prime(11))

  def test25(self):
    self.assertFalse(is_prime(25))

  def test28(self):
    self.assertFalse(is_prime(28))

if __name__ == "__main__":
  unittest.main()

  

  