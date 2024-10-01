from common.path_handler import path_handler
import streamlit as st


if __name__ == "__main__":
    st.sidebar.image(path_handler.profile_file_path)
    st.title("个人介绍")
    st.markdown("###")
    st.markdown("### 学历:&ensp;硕士")
    st.markdown("### 学校:&ensp;上海交通大学(SJTU)")
    st.markdown("### 专业:&ensp;电子信息")
