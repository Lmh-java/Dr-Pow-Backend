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
        temperature=0.3,
        messages=[
            {"role": "system",
             "content": "You are a helpful assistant. Your expertise is in in summarizing texts and parsing information into JSON."},
            {"role": "user", "content":
                """
You will summarize provided content using a title and multiple bullet points and convert the content to the following JSON format. You will also follow an additional prompt provided by the user at the end of this input, which will augment or elaborate on some of the instructions provided below. If the user does not provide an additional prompt, you may ignore it. 
The summary will follow the following specifications:
- The summary will cover the text in the order that it is presented. 
- The summary will generate a relevant title that is AT MOST 10 characters
- The summary will provide 2-4 bullet points in each slide that is relevant to the title
You will need to replace the text in square brackets [] with your generated text. Here is the format of the JSON that you will need to convert to:
{
   "presentation theme": "[theme]", 
   "presentation slides": [
       {"title": "[title]", "body": ["[point with keywords]", "[point with keywords]", "[point with keywords]"]}, 
       {"title": "[title]", "body": ["[point with keywords]", "[point with keywords]", "[point with keywords]"]}
   ]
}
Here is the content, surrounded by curly braces:
{
                """
                + content[:3000] +
                """
}
The additional prompt will now be provided in curly braces. If there is nothing in the curly braces, you may ignore the additional prompt. Here is the additional prompt: {                
                """
                + additional_prompt +
                "}"
            },
        ]
    )
    return completion.choices[0].message
