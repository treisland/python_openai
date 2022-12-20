# Python Open AI.

Interact with the Open AI API using python.
Utility scripts are provided that allow you to interact directing via the command line.

## Requirements
Install openai library

`pip install --upgrade openai`

## Environment Variables
Add the following environment variables
| variables | description |
| --- | --- |
| OPENAI_API_KEY | bearer token for openAI |
| OPENAI_HOME | folder path where this source code is located on your machine |

## (Optional) Update System PATH
If you wish to call scripts directly from the command line then add the **scripts** directory to your path.


PATH=$PATH;$OPENAI_HOME/scripts 

---

## How to use CLI
Using the CLI is easy. Just call on of files located in the **/scripts** directory 

Syntax: `openai "<command>"`

```
PS D:\dev\openai> scripts/openai.ps1 "generate a todo list for traveling to france"


1. Research visa requirements 
2. Book flights 
3. Make hotel reservations 
4. Purchase travel insurance 
5. Learn some basic French phrases 
6. Pack appropriate clothing 
7. Exchange currency 
8. Research attractions and activities 
9. Make a list of must-see places 
10. Download a map of France
```

```
PS D:\dev\openai> scripts/openai.ps1 "generate a resume for a dog walker" 


John Doe

Dog Walker

Summary

I am an experienced and passionate dog walker with a deep love for animals. I have a strong commitment to providing the best care for each and every dog I walk. I am reliable, organized, and have a great eye for detail. I am confident that I can provide the highest quality of care for your pet.

Experience

Dog Walker, ABC Pet Care, 2020-Present

• Walked dogs of all sizes and breeds

• Followed all safety protocols and guidelines

• Ensured that all dogs were properly hydrated and exercised

• Cleaned up after each walk

• Monitored the health and wellbeing of each dog

• Administered medications as needed

• Maintained detailed records of each walk

• Developed strong relationships with clients

• Provided excellent customer service

Dog Walker, XYZ Pet Services, 2018-2020
```