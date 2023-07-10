import openai
from dotenv import dotenv_values
from colorama import init, Fore

init()
config = dotenv_values(".env")
openai.api_key = config["openAI_API_Key"]


def green(str):
    return Fore.GREEN + str


def blue(str):
    return Fore.BLUE + str


initial_prompt = "You are a friendly and helpful chatbot and your name is Sara"
history = [{"role": "system", "content": initial_prompt}]

while True:
    try:
        user_input = input(blue("You: "))
        history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-4", max_tokens=500, stream=True, messages=history
        )
        print(green("Sara:"), end=" ")
        for chunk in response:
            if "role" in chunk["choices"][0]["delta"]:
                continue
            elif "content" in chunk["choices"][0]["delta"]:
                text = chunk["choices"][0]["delta"]["content"]
                history.append({"role": "assistant", "content": text})
                print(green(text), end="", flush=True)

        print()

    except KeyboardInterrupt:
        print("Exiting...")
        break
