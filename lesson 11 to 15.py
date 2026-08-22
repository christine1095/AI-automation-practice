# import  requests
# url = "http://api.open-notify.org/astros.json"
# print("connectin to the network")
# response = requests.get(url)

# data = response.json()
# print(data)

# no_of_astronauts = data["number"]
# list_of_people = data["people"]

# print(f"\n success there arecurrently {no_of_astronauts} human in space right now.")

# print("\n here are there names:")

# for person in list_of_people:
#     print(f"{person['name']} on the  board the { person['craft'] } ")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
# #Weather
# import requests

# url = "https://open-meteo.com"

# print("gweting weather forcast")
# response = requests.get(url)

# data = response.json()

# current = data ["current"]

# temp = current["temperature_2m"]
# wind = current["wind_speed_10"]
# direction = current["wind direction_10m"]

# print(f"current temp: {temp}")
# print(f"current temp: {wind}")
# print(f"current temp: {direction}")
########################################################
# import requests

# url = "https://api.open-meteo.com/v1/forecast?latitude=43.5890&longitude=-79.6441&current=temperature_2m,wind_speed_10m,wind_direction_10m"

# print("Getting weather forecast...")

# response = requests.get(url)
# data = response.json()

# current = data["current"]

# temp = current["temperature_2m"]
# wind = current["wind_speed_10m"]
# direction = current["wind_direction_10m"]

# print(f"Current temperature: {temp}°C")
# print(f"Wind speed: {wind} km/h")
# print(f"Wind direction: {direction}°")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #lesson 13 security hide
# import os 
# from dotenv import load_dotenv
# from openai import OpenAI
 
# load_dotenv()

# try:
#     print("Initializing secure back systems....")

#     secure_key = os.getenv("My_secret_key")
#     if secure_key is None:
#         raise ValueError("API track key not found inside the the hidden environment")

#     client = OpenAI(api_key=secure_key)
#     print("\n [Success] Security verification passed")
#     print(" Client configuredcompletely using hiddem  background token")

# except ValueError as  security_error:
#     print("\n [Security Sheil Alert]")
#     print(f"ReSON: {security_error}")
#     print("Fix required Double check your hidden '.env' file parameters")
#________________________________________________________________________________________
# # #lesson 14 promp engineering inside python
# # import os 
# # from dotenv import load_dotenv
# # from openai import OpenAI
 
# # load_dotenv()
# # secure_key = os.getenv("My_secret_key")
# # client = OpenAI(api_key=secure_key)
# # try:
# #     print("Initializing secure back systems....")

# #     response = client.chat.completions.create(
# #         model="gpt-4o-mini"
# #         temperature=0.3
# #         messages=[
# #             {
# #                 "role": "system",
# #                 "content": "You are sarcastic, grumpy IT assistant who talk like a pirate.Keep answer very short."
# #             },
# #             {
# #                 "role:" "user",
# #                 "content": "Why is my internet slow?"
# #             }
# #         ]
# #     )

# #     ai_answer = response.choices[0].messae.content
# #     print("\n Ai response")
# #     print(ai_answer)
# #     print("____________")

# # except Exception as error:
# #     print("\n [Security Sheil Alert]")
# #     print(f"lesson 13 Error: {error}")
# #++++++++++++++++++++++++++++++++++++++++++++++++
# #Lesson 14.1
# # Lesson 14 - Prompt Engineering Practice

# import os
# from dotenv import load_dotenv

# load_dotenv()

# secure_key = os.getenv("My_secret_key")

# print("API key loaded:", secure_key is not None)

# try:
#     print("Initializing secure backend systems....")

#     # Practice prompt
#     system_prompt = (
#         "You are a sarcastic, grumpy IT assistant "
#         "who talks like a pirate. Keep answers very short."
#     )

#     user_prompt = "Why is my internet slow?"

#     # Mock AI response for Python practice
#     ai_answer = "Arrr! Probably your Wi-Fi be struggling with a weak signal, matey!"

#     print("\nAI Response:")
#     print(ai_answer)
#     print("____________")

# except Exception as error:
#     print("\n[Security Shield Alert]")
#     print(f"Lesson 14 Error: {error}")
#_____________________________________________________________
# #lesson 14 promp engineering inside python
# import os 
# from dotenv import load_dotenv
# from openai import OpenAI
 
# load_dotenv()
# secure_key = os.getenv("My_secret_key")
# client = OpenAI(api_key=secure_key)
# try:
#     print("Initializing secure back systems....")

#     response = client.chat.completions.create(
#         model="gpt-4o-mini"
#         temperature=0.3
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are sarcastic, grumpy IT assistant who talk like a pirate.Keep answer very short."
#             },
#             {
#                 "role:" "user",
#                 "content": "Why is my internet slow?"
#             }
#         ]
#     )

#     ai_answer = response.choices[0].messae.content
#     print("\n Ai response")
#     print(ai_answer)
#     print("____________")

# except Exception as error:
#     print("\n [Security Sheil Alert]")
#     print(f"lesson 13 Error: {error}")
#++++++++++++++++++++++++++++++++++++++++++++++++
#Lesson 14.1
# Lesson 14 - Prompt Engineering Practice

# Lesson 14 - Prompt Engineering with Gemini

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load .env
load_dotenv()

# Get API key securely
secure_key = os.getenv("My_secret_key")
client  = genai.Client(api_key=secure_key)

print("API key loaded:", secure_key is not None)

try:
    print("Initializing secure backend systems....")

    # Create Gemini client
    client = genai.Client(api_key=secure_key)

    # Send prompt to Gemini
    chat = client.chats.create(
        model="gemini-3.6-flash",
        config={
            "temperature": 0.3,
            "system_instruction": (
                "You are a friendly and professional IT assistant. "
                "Speak naturally and casually, like a helpful human coworker. "
                "Be polite, clear, and approachable. "
                "Keep responses concise and easy to understand. "
                "Do not use sarcasm, insults, pirate language, or rude comments."

            )
        }
    )
    while True:
        User_input = input(("You: "))
        if User_input.lower() == 'quit':
            print("Goodbye matey!")
            break

        response = chat.send_message(User_input)

        print("\nAI Response:")
        print("-" * 30)
        print(response.text)
        print()
    

except Exception as error:
    print("\n[Security Shield Alert]")
    print(f"Lesson 15 Error: {error}")