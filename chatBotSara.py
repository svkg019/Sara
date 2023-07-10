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
messages = [{"role": "system", "content": initial_prompt}]

while True:
    try:
        user_input = input(blue("You: "))
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model="gpt-4",max_tokens=500,messages=messages)
        messages.append(response.choices[0].message.to_dict())
        print(green("Sara: "), response.choices[0].message.content)
    except KeyboardInterrupt:
        print("Exiting...")
        break
