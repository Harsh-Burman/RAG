from openai import OpenAI

api_key = "csk-2en3te2m2rnp3x69xtvt8hf5tw6ct9445t333ev3m2per49e"
base_url = "https://api.cerebras.ai/v1"
model="llama3.1-8b"

client = OpenAI(api_key=api_key, base_url=base_url)

prompt = input("\n>> ")

while prompt.strip().lower() != "exit":

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    print(response.choices[0].message.content)

    prompt = input("\n>> ")