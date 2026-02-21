
class TestUtils:
    def __init__(self) -> None:
        self._messages = [
            "Dear SBI User, your A/c X9590-credited by Rs.45 on 15Feb26 transfer from PRABHAT GUPTA Ref No 897106530663 -SBI",
            "Dear UPI user A/C X9590 debited by 614.42 on date 05Feb26 trf to MPOKKET FINANCIA Refno 765472268909 If not u? call-1800111109 for other services-18001234-SBI",
            "Dear UPI user A/C X9590 debited by 5000.00 on date 04Feb26 trf to RIYA KUMARI Refno 100864957703 If not u? call-1800111109 for other services-18001234-SBI"
        ]

    def get_messages(self) -> list[str]:
        return self._messages