from openai import OpenAI
import os

#os.environ["OPENAI_API_KEY"] = "sk-proj-**********************"

client = OpenAI()

def main():
    print("라즈베리파이 OpenAI 챗봇. 종료: quit/exit\n")
    history = [
        {"role": "system", "content": "너는 한국어로 답변하는 챗봇이다."}
    ]

    while True:
        try:
            user_input = input("You: ").strip()
        except:
            break

        if user_input.lower() in ["quit", "exit"]:
            break

        if not user_input:
            continue

        history.append({"role": "user", "content": user_input})

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=history
        )

        answer = response.output_text
        print("Bot:", answer, "\n")

        history.append({"role": "assistant", "content": answer})

if __name__ == "__main__":
    main()

