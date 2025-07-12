# Call GPT-3.5 or GPT-4 to generate response
def generate_agent_reply(user_input):
    import openai
    import sys
    sys.path.append("..")  # Optional, only if using config file

    from utils import config
    openai.api_key = config.OPENAI_API_KEY

    system_prompt = (
        "You are a helpful and empathetic AI voice assistant trained to help customers with billing-related concerns. "
        "Keep responses short, clear, and reassuring."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.6,
        max_tokens=100
    )

    reply = response['choices'][0]['message']['content'].strip()
    return reply
