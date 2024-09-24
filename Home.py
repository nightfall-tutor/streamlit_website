from lib.basic_functions import update_visitor_count
import os.path
import streamlit as st


if __name__ == "__main__":
    update_visitor_count()
    st.sidebar.image(os.path.join(os.path.dirname(__file__), "resources", "profile.jpg"))
    # st.title("留学生作业/考试/论文/课设辅导答疑代写")
    # st.header("个人写手NightFall")



