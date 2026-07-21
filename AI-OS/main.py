from startup import start
from memory import load_user, save_user
from engine import AIEngine

start()

user = load_user()

if "name" not in user:

    user["name"] = input("Tumhara naam kya hai : ")

    save_user(user)

name = user["name"]

print("Welcome", name)

ai = AIEngine(name)

while True:

    question = input(f"{name} : ")

    answer = ai.process(question)

    print("AI :", answer)

    if question.lower() == "bye":

        break
