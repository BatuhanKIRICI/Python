from data import question_data
from question_model import Question


question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank[0])
