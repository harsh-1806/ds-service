import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

from services.Expense import Expense

class LLMService:
    def __init__(self) -> None:
        load_dotenv()
        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
                ),
                (
                    "human","{text}"
                )
            ]
        )

        self.apiKey = os.getenv("OPENAI_API_KEY")
        self.llm  = ChatMistralAI(api_key=self.apiKey, model_name="mistral-large-latest")
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expense)

    def runLLM(self, message):
            return self.runnable.invoke({"text":message})