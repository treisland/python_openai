import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

def app():

  if os.name == "nt": 
        os.system('cls')
  else:
    os.system('clear')

  print("--OPEN AI Bot--\n")

  return botLoop()

def botLoop():

  instruction="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
  prompt=instruction

  print("- \"!new\" to start a new conversation")
  print("- \"!exit\" to terminate")
  print("____________________________________")
  while True:


    human_input = input("\nHuman: ")

    if human_input.lower() =="!exit": 
      return False

    elif human_input.lower() =="!new": 
      return True

    prompt = "".join([prompt, "\n", human_input])

    bot=openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      max_tokens=2048,
      temperature=.6
    )

    bot_response = bot["choices"][0]["text"]

    print(f'\nAI: {bot_response}')

    prompt = "".join([prompt, "\n", bot_response])

if __name__ == "__main__":

  again = True

  while again:
    again = app()