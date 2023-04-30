from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
def openai_response(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": f"{prompt}"}],
        temperature=0.9,
        max_tokens=100  
    )
    # response_dict = response['choices']
    # if response_dict and len(response_dict) > 0:
    prompt_response = response['choices'][0]['message']['content']
    return prompt_response