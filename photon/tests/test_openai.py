import os

import openai

from photon import Photon

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
openai = Photon(openai, disable=True)

response = openai.Completion.create(
    engine="davinci",
    prompt="This is a test",
    max_tokens=50,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\n"],
)


if __name__ == "__main__":

    print("=====================================")
    print("✅ OpenAI Completion Create Output:")
    print(response)
    print("=====================================")