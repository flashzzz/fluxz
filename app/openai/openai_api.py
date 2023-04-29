from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
def openai_response(prompt):
    response = openai.Completion.create(
        model='gpt-3.5-turbo',
        prompt=prompt,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        stop=['\n', " Human:", " AI:"]
    )
    response_dict = response.get('choices')
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0].get('text')
    return prompt_response