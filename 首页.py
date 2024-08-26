import os.path
from lib.data_handler import DataHandler
import streamlit as st


if __name__ == "__main__":
    st.sidebar.image(os.path.join(os.path.dirname(__file__), "static", "Profile.jpg"))
    st.title("留学生作业/考试/论文/课设辅导答疑代写")
    st.header("个人写手NightFall")


