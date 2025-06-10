from openai import OpenAI

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  model="gpt-4.1-mini",
  input=["Generate a random name "],
  text={
    "format": {
      "type": "text"
    }
  },
  reasoning={},
  tools=[],
  temperature=1,
  max_output_tokens=20,
  top_p=1,
  store=True
)

print(response)

