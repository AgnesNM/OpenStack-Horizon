Horizon uses the Python version installed globally in your laptop if installed locally?
- Check Python version (if older install mock from PyPi)
- Different assert methods for different scenarios (testing for None, vs equality, existence, truthiness, falsiness)
- Check the rest of the code base (didn't use the unitttest.mock base class, Mock)
- The code imported mock, so we use mock.Mock
- If I import Mock, as in from unittest.mock import Mock
- If I import MagicMock, as in from unittest.mock import MagicMock
