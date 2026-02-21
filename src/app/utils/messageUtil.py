import re

class MessageUtils:
    def isBankSms(self, message: str) -> bool:
        message = message.lower()
        return RuleEngine.score(message) >= 2

class RuleEngine:
    @staticmethod
    def score(message: str) -> int:
        message = message.lower()
        score = 0

        patterns = {
            "keyword": r'\b(debited|credited|spent|withdrawn|deposit|transaction)\b',
            "amount": r'(rs\.?|inr|\₹)\s?\d+',
            "account": r'(xx|x{2,}|\*{2,})\d{2,4}',
            "txn_id": r'(txn|transaction)\s?id',
            "upi": r'\b(upi|neft|rtgs|imps)\b',
            "otp": r'\botp\b'
        }

        if re.search(patterns["keyword"], message): score += 1
        if re.search(patterns["amount"], message): score += 1
        if re.search(patterns["account"], message): score += 1
        if re.search(patterns["txn_id"], message): score += 1
        if re.search(patterns["upi"], message): score += 1
        if re.search(patterns["otp"], message): score -= 1

        return score