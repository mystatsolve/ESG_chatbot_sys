import openai

openai.api_key = "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"  # Add your OpenAI API key here

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """넌 ESG 전문가야. 한국기업의 ESG관련 질문에 적절한 답변을 해줘' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
