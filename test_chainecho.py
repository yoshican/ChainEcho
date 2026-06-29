# test_chainecho.py
"""
Tests for ChainEcho module.
"""

import unittest
from chainecho import ChainEcho

class TestChainEcho(unittest.TestCase):
    """Test cases for ChainEcho class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainEcho()
        self.assertIsInstance(instance, ChainEcho)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainEcho()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
