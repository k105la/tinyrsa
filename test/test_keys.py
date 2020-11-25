#!/usr/bin/env python
import unittest
from tinyrsa.generate_keys import TinyKeys

class TestTinyKeys(unittest.TestCase):

    def setUp(self):
        self.test_keys = TinyKeys()
        
    def test_public_key(self):
        p = self.test_keys.phi
        self.pub_n, e = self.test_keys.public_key()
        self.assertTrue(1 < e < self.pub_n)
        return self.pub_n

    def test_private_key(self):
        pub_n = self.test_public_key()
        priv_n, d = self.test_keys.private_key()    
        self.assertEqual(priv_n, pub_n)

if __name__ == "__main__":
    unittest.main()
