Horizon uses the Python version installed globally in your laptop if installed locally?
- Check Python version (if older install mock from PyPi)
- Different assert methods for different scenarios (testing for None, vs equality, existence, truthiness, falsiness)
- Check the rest of the code base (didn't use the unitttest.mock base class, Mock)
- The code imported mock, so we use mock.Mock or mock.MagicMock
- If I import Mock, as in from unittest.mock import Mock, then I can use Mock
- If I import MagicMock, as in from unittest.mock import MagicMock, then I can use MagicMock
- MagicMock is an extension of Mock, and has more "bells and whistles" which could break your tests, or cause some to pass/fail due to default MagicMock behaviour.
- MagicMock also has built in implementations to support magic methods
- MagicMock - better used with context managers?
- Is mocking more like imitating the functionality of a function/class/library
- What's the difference between mocking and patching?
- Prerequisites, unittesting in python, mocking, Mock, MagicMock, and patching
- Steps when mocking
-- Set up mocks for dependencies
-- Configure expected behavior of mocks
-- Call your actual function/method under test
-- Verify that your actual code interacted correctly with the mocks
-- Assert on the results of your actual function
  
- OpenStack Horizon doesn't use models, instead we access various services via API calls. We would access volumes via the cinder api, for example.
## Patching
- I think we use patching when we want to mock something that we are importing from another part of the code.
- @patch.object() takes two or three parameters: "The three argument form takes the **object to be patched**, **the attribute name** and the **object to replace the attribute with**"
- When calling with the two argument form you *omit the replacement object*, and a mock is created for you and passed in as an extra argument to the decorated function
- In our example, *@mock.patch.object(cinder, 'volume_get')* "cinder" is the object we want to patch, and "volume_get" is its attribute.
    ```python
    @mock.patch.object(cinder, 'volume_get')
    def test_no_attachment(self, mock_no_attachment):
        column = volume_tables.AttachmentColumn("attachments") #an instance of the attachment column
        volume = mock_no_attachment.return_value
        volume.attachments = []
        result = column.get_raw_data(volume)
        self.assertIsNone(result, None)
    ```
- *def test_no_attachment(self, mock_no_attachment):* "mock_no_attachment" is a mock which is the result of "cinder.volume_get"
- We assign the result of "mock_no_attachment" to "volume" since, it's essentially volume information *volume = mock_no_attachment.return_value*
- Pass "volume" (mocked volume info) to our real function, "get_raw_data": *result = column.get_raw_data(volume)*
- 
