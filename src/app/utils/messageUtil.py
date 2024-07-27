import re

class MessageUtils:
    def isBankSms(self, message):
        word_to_search = ['spent', 'debited', 'card', 'bank', 'credited']
        pattern = r'\b(?:' + '|'.join(re.escape(word) for word in word_to_search) + r')\b'
        match = re.search(pattern, message, flags=re.IGNORECASE)
        return bool(match)
    
