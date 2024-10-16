from common.database_connector import DatabaseConnector
import streamlit as st
import datetime
import uuid
import time


@st.cache_data
def get_random_seed():  # 基于uuid全局标识符和当前时间戳生成随机种子
    random_seed = f"{uuid.uuid4()}-{int(time.time() * 1000)}"
    print(random_seed)
    return random_seed


@st.cache_resource
def get_database_connector(host, user, password, database):
    return DatabaseConnector(host, user, password, database)


@st.cache_data
def update_visitor_count():
    pass


@st.cache_data
def update_clicker_count():
    pass


@st.cache_data
def update_contact_information(new_contact_information: str):
    pass
    # data_handler.update_contact_information(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {new_contact_information}")






