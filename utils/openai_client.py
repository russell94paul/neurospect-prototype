import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)

def call_openai(prompt: str, input_text: str, model: str = None, temperature: float = None, max_tokens: int = None) -> str:
    model = model or os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    temperature = float(temperature if temperature is not None else os.getenv('TEMPERATURE', 0.0))
    max_tokens = int(max_tokens if max_tokens is not None else os.getenv('MAX_TOKENS', 800))

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input_text}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content.strip()