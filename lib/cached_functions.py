import streamlit as st
import uuid
import time


@st.cache_data
def get_random_seed():  # 基于uuid全局标识符和当前时间戳生成随机种子
    random_seed = f"{uuid.uuid4()}-{int(time.time() * 1000)}"
    print(random_seed)
    return random_seed



