from core.ai_engine import ask_question

print("================================")
print("        AfriMind AI v28.1")
print(" Building Intelligence for Africa")
print(" Type exit to close")
print("================================")


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("AfriMind: Goodbye!")
        break

    answer = ask_question(question)

    print("\nAfriMind:", answer)