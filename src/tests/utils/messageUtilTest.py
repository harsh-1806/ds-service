import unittest

from tests.messages import TestUtils
from app.utils.messageUtil import MessageUtils


class MessageUtilTest(unittest.TestCase):
    def testIsBankSms(self):
        testUtils = TestUtils()
        messagesForTest = testUtils.get_messages()
        utils = MessageUtils()
        self.assertTrue(utils.isBankSms(messagesForTest[1]), msg= f"{messagesForTest[1]} is not a BankSms message")


if __name__ == '__main__':
    unittest.main()
