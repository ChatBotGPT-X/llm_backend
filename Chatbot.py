from http.client import responses

from langchain.chains.summarize.refine_prompts import prompt_template
from openai import OpenAI, api_key, models
import streamlit as st
from langchain_openai import ChatOpenAI
from prompt.ingnok import  INGNOK_PROMPT
from langchain.prompts import PromptTemplate
from resources.data import  data
import time
# 初始化会话状态
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# 默认用户
USERNAME = "admin"
PASSWORD = "5201314"


# 登录页面
def login():
    st.header("登录")
    st.divider()

    username = st.text_input("用户名")
    password = st.text_input("密码", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("登录成功!")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("用户名或密码错误")

page1 = st.Page("pages/chat_bot.py", title="售后服务")


login_page = st.Page(login, title="登录")
pg = st.navigation([login_page])
if st.session_state.logged_in:
    pg = st.navigation({"主要功能": [page1]})

pg.run()
