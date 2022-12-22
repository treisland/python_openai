# Python Open AI.

Interact with the Open AI API using python.
Utility scripts are provided that allow you to interact directing via the command line.

Currently it uses the **text-davinci-003** model

## Requirements
Install openai library

`pip install --upgrade openai`

## Environment Variables
Add the following environment variables
| variables | description |
| --- | --- |
| OPENAI_API_KEY | bearer token for openAI |
| OPENAI_HOME | folder path where this source code is located on your machine |


## How to use CLI
This program functions as a loop and let's you ask follow-up questions.

directory 

Syntax: 
```
openai_cli.py
```

> Enter "!new" in the prompt to start a new conversation / thread.
>
> Enter "!exit" to quit the program.

Command line interface
```
Python Open AI Bot

- "!new" to start a new conversation
- "!exit" to terminate
____________________________________

Human: write me a tag-line for an icecream shop

AI:
"Cool down with our delicious ice cream!"

Human: another that is funny

AI:

"Ice cream so good, it's criminal!"

```