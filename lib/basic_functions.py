from common.data_handler import data_handler
import streamlit as st
import datetime
import uuid
import time


@st.cache_data
def get_random_seed():  # 基于uuid全局标识符和当前时间戳生成随机种子
    random_seed = f"{uuid.uuid4()}-{int(time.time() * 1000)}"
    print(random_seed)
    return random_seed


@st.cache_data
def update_visitor_count():
    data_handler.update_visitor_count()


@st.cache_data
def update_clicker_count():
    data_handler.update_clicker_count()


@st.cache_data
def update_contact_information(new_contact_information: str):
    data_handler.update_contact_information(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {new_contact_information}")






