
import streamlit as st
from langchain_openai import ChatOpenAI
from prompt.ingnok import  INGNOK_PROMPT
from langchain.prompts import PromptTemplate
from resources.data import  data



st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by OpenAI")

llm = ChatOpenAI(
    api_key="sk-xT5DaSCFdh4UulSjZy8dF7PZFtBnnXz9I7HVBovh1dBHSynF",
    base_url = "https://api.moonshot.cn/v1",
    model="moonshot-v1-8k",
)
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    system_prompt_template = PromptTemplate.from_template(INGNOK_PROMPT)
    system_prompt = system_prompt_template.format(question=prompt,content=data)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    stream = llm.stream(system_prompt)
    st.write_stream(stream)

    #responses = llm.invoke(system_prompt)
    # response = client.cha
    # t.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    #msg = responses.content
    #st.session_state.messages.append({"role": "assistant", "content": msg})
    #st.chat_message("assistant").write(msg)