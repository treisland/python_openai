import os
import openai
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")
r=openai.Completion.create(
  model="text-davinci-003",
  prompt=sys.argv[1],
  max_tokens=200,
  temperature=0
)

print(r["choices"][0]["text"])
