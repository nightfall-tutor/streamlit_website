from common.path_handler import path_handler
import streamlit as st
import os.path


if __name__ == "__main__":
    st.set_page_config(page_title="个人介绍 留学课程作业考试辅导答疑家教 个人老师", page_icon="🧑‍🎓")
    st.title("个人介绍")
    st.sidebar.image(path_handler.profile_file_path)
    st.markdown("###")
    st.markdown("### 👨‍🎓学历:&ensp;硕士")
    st.markdown("### 🏫学校:&ensp;上海交通大学（SJTU）")
    st.markdown("### 📚专业:&ensp;电子信息")
    st.image(os.path.join(path_handler.resources_folder_path, "self_introduction_1.jpg"))
    st.image(os.path.join(path_handler.resources_folder_path, "self_introduction_2.jpg"))
    st.image(os.path.join(path_handler.resources_folder_path, "self_introduction_3.jpg"))

