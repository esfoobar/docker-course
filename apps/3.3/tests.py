# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest

from counter.tests import CounterTest

if __name__ == '__main__':
    unittest.main()
