import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:

  if os.name == "nt": 
    os.system('cls')
  else:
    os.system('clear')

  print("--OPEN AI Bot--\n\n")
  cmd = input("What is your command? ")

  if cmd.lower() =="exit": 
    break

  bot=openai.Completion.create(
    model="text-davinci-003",
    prompt=cmd,
    max_tokens=2048,
    temperature=.6
  )

  bot_response = bot["choices"][0]["text"]
  print(f'\nBot: {bot_response}')


  print("\n____________________")

  cmd = input('\nContinue (y/n)? ')

  if(cmd.lower() == "n"):
    break
