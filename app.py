from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage
thread_id="1"
config={"configurable":{"thread_id":thread_id}}
response = chatbot.invoke({'messages':[HumanMessage(content="What is the capital of India")]}, config=config)

print(response['messages'][-1].content)
