import json
import random
from pydantic import BaseModel, Field
from typing import List
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI


class QA(BaseModel):
    question: str = Field(description="question")
    answer: str = Field(description="answer")


class QAs(BaseModel):
    items: List[QA]


class Quiz:
    asked = set()
    question_bank: QAs
    llm: ChatOpenAI

    def __init__(self, question_bank):
        self.llm = ChatOpenAI(
            temperature=0, model_name="gpt-3.5-turbo", max_tokens=1500
        )
        self.question_bank = question_bank

    def quiz_and_give_answer(self):
        if len(self.asked) == 100:
            print("All questions asked. You're done!")
            return True
        random_index = random.randint(0, len(self.question_bank.items) - 1)
        while random_index in self.asked:
            random_index = random.randint(0, len(self.question_bank.items) - 1)
        self.asked.add(random_index)
        qa = self.question_bank.items[random_index]
        user_answer = input(qa.question + " Answer: ")
        check_answer_prompt = PromptTemplate(
            input_variables=["question", "answer", "user_answer"],
            template="You will be given a pair of question and answer, as well as a user's answer. Return if the user's answer is correct or not and explain why. Question: {question}\n Answer: {answer}\n User's answer: {user_answer}",
        )
        chat_input = check_answer_prompt.format_prompt(
            question=qa.question, answer=qa.answer, user_answer=user_answer
        )
        response = self.llm.predict(chat_input.to_string())
        print(response)
        return False

    def run_quiz(self):
        finished = False
        while not finished:
            finished = self.quiz_and_give_answer()


if __name__ == "__main__":
    with open("data.json", "r") as f:
        json_data = json.load(f)
    question_bank = QAs(**json_data)
    q = Quiz(question_bank=question_bank)
    q.run_quiz()
