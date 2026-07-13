from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st
import uuid



def generate_thread_id():
    return str(uuid.uuid4())


#Add a new thread Id to the conversation list
def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)



st.title("Agentic chatbot with Langgraph")
CONFIG={'configurable':{'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

#Create a loist for storing all conversation thread IDs
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads']=[]

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# ========================= Sidebar threading feature =========================

# Display the sidebar title
st.sidebar.title("My Conversations")

# Create a button for starting a new conversation
if st.sidebar.button("New Chat"):

    # Reset the current chat and create a new thread
    reset_chat()

    # Rerun the Streamlit app to update the interface
    st.rerun()





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