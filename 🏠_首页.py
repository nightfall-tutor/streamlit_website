from symbol import parameters

from lib.basic_functions import update_visitor_information
from common.path_handler import path_handler
from common.secret_handler import secret_handler
import streamlit as st
import pandas as pd


if __name__ == "__main__":
    st.set_page_config(page_title="首页 留学课程作业考试辅导答疑家教 个人老师", page_icon="🏠")
    st.header(body="留学课程作业考试辅导答疑家教")
    secret_handler.db_host = st.secrets["db_host"]
    secret_handler.db_username = st.secrets["db_username"]
    secret_handler.db_password = st.secrets["db_password"]
    secret_handler.db_database = st.secrets["db_database"]
    secret_handler.email_sender = st.secrets["email_sender"]
    secret_handler.email_password = st.secrets["email_password"]
    secret_handler.email_receiver = st.secrets["email_receiver"]
    update_visitor_information()

    st.sidebar.image(path_handler.profile_file_path)
    st.markdown("### 课程📚/作业🖋️/考试💯/论文📃/课设⚗️/实验🔬")
    st.markdown("### 一对一💁‍♂️/一对多👪")
    st.markdown("###")
    st.markdown("### 🧑‍🏫个人老师 🧑‍🎓硕士学历")
    st.markdown("### 🙅‍♂️不是机构 🙅‍♀️不是中介")
    st.markdown("### 🙋只接会的 ❌不找外包")
    st.markdown("### 🤝诚信接单 🧑‍🤝‍🧑互利双赢")
    st.markdown("###")
    st.markdown("### 📖擅长课程")
    st.markdown("#### ➕数学类")
    st.dataframe(
        pd.DataFrame(
            [
                ["Calculus", "微积分"],
                ["Advanced Mathematics", "高等数学"],
                ["Mathematics Analysis", "数学分析"],
                ["Linear Algebra", "线性代数"],
                ["Theory of Matrix", "矩阵理论"],
                ["Theory of Probability", "概率论"],
                ["Statistics", "统计"],
                ["Differential Equation", "微分方程"],
                ["Physics", "物理"],
                ["Fundamentals of Circuits", "电路基础"]
            ],
            columns=["Mathematics & Physics", "数理类"]
        ),
        width=10000,
        hide_index=True
    )
    st.markdown("#### ⌨️编程类")
    st.dataframe(
        pd.DataFrame(
            [
                ["Matlab", "Matlab"],
                ["Java", "Java"],
                ["Python", "Python"],
                ["Data Structure", "数据结构"],
                ["Algorithm", "算法"]
            ],
            columns=["Programming", "编程类"]
        ),
        width=10000,
        hide_index=True
    )
    st.markdown("#### 🛠️工科类")
    st.dataframe(
        pd.DataFrame(
            [
                ["Theory of Control", "控制理论"],
                ["Theory of Linear System", "线性系统理论"],
                ["Numerical Method", "数值方法"]
            ],
            columns=["Engineering", "工科类"]
        ),
        width=10000,
        hide_index=True
    )
    st.markdown("""
    以上仅列出部分课程，可带课程名咨询，有把握就接~
    """)



