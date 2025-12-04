import time
import random
from google import genai

client = genai.Client(api_key="aaa")

def print_llm_response(prompt):
    MAX_RETRIES = 5
    INITIAL_WAIT_TIME = 2
    
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            print("-" * 100)
            print(response.text)
            print("-" * 100)
            print("\n")
            return
        
        except genai.errors.APIError as e:
            print(f"Erro da API do Gemini: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def get_llm_response(prompt):
    MAX_RETRIES = 5
    INITIAL_WAIT_TIME = 2
    for attempt in range(MAX_RETRIES):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except genai.errors.APIError as e:
            return f"Erro da API do Gemini: {e}"
        except Exception as e:
            return f"Erro inesperado: {e}"


def get_chat_completion_recommended(prompt, chat_session):
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except genai.errors.APIError as e:
        return f"Erro da API do Gemini: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"
    
def get_chat_completion_corrected(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_with_history
    )
    return response.text