from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

from util.config import Config

client = None
if not client:
    client = OpenAI(api_key=Config.OPEN_AI_API_KEY)


# query chatgpt 3.5 and return a json
def query_chatgpt3_5(content: str, additional_prompt: str) -> ChatCompletionMessage:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant. You expertise in summarizing texts and parse information into json"},
            {"role": "user", "content":
                """
                Summarize using 3-5 keywords each and convert the content to the following format (
                """
                + additional_prompt +
                """):
               {"presentation theme": "[theme]", "presentation slides": [{"title": "[title]", "body": ["[point with keywords]", "[point with keywords]", "[point with keywords]"]}, {"title": "[title]", "body": ["[point with keywords]", "[point with keywords]", "[point with keywords]"]}]}
               Here is the content:
               {
                """
                + content + "}"
             },
        ]
    )
    return completion.choices[0].message
