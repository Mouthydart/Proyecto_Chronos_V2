from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

async def generate_motivational_phrase(user_text: str):
    try:

        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": ("Eres un asistente empático el usuario te contará su día, responde con una única frase de aliento corta y motivadora.")
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ],
            max_tokens=60,
            temperature=0.7
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error con la IA: {e}")

        return "¡Eres capaz de lograr todo lo que te propongas hoy!"