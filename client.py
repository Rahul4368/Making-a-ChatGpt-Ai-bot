from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)