import dotenv
from langchain_deepseek import ChatDeepSeek

dotenv.load_dotenv()

model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to Chinese."),
    ("human", "I love programming."),
]
result = model.invoke(messages)

print(result)
