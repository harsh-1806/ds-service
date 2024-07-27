from services.LLMService import LLMService
from utils.messageUtil import MessageUtils

class MessageService:
    def __init__(self) -> None:
        self.messageUtil = MessageUtils()
        self.llmService = LLMService()

    def process_message(self, message):
        if self.messageUtil.isBankSms(message) :
            return self.llmService.runLLM(message)
        else :
            return None