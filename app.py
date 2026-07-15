from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st

# thread_id="1"
# config={"configurable":{"thread_id":thread_id}}
# response = chatbot.invoke({'messages':[HumanMessage(content="What is the capital of India")]}, config=config)

# print(response['messages'][-1].content)


st.title("Agentic chatbot with Langgraph")
CONFIG={'configurable':{'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


st.title("Agentic chatbot with Langgraph")
user_input= st.chat_input('Type here')
st.write('User: ', user_input )
if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)


     # first add the message to message_history
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})