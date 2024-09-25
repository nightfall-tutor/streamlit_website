from lib.basic_functions import update_visitor_count
import os.path
import streamlit as st
import pandas as pd


if __name__ == "__main__":
    update_visitor_count()
    st.sidebar.image(os.path.join(os.path.dirname(__file__), "resources", "profile.jpg"))
    st.title("🏫留学生辅导答疑")
    st.markdown("### 课程📚/作业🖋️/考试💯/论文📃/课设⚗️/实验🔬")
    st.markdown("###")
    st.markdown("### 🧑‍🏫个人老师 🧑‍🎓硕士学历")
    st.markdown("### 🙅‍♂️不是机构 🙅‍♀️不是中介")
    st.markdown("### 🤝诚信接单 🧑‍🤝‍🧑互利双赢")
    st.markdown("###")
    st.markdown("### 📖擅长课程")
    st.markdown("#### ➕数学类")
    st.table(
        pd.DataFrame(
            [
                ["Calculus 微积分"],
                ["Advanced Mathematics 高等数学"],
                ["Mathematics Analysis 数学分析"],
                ["Linear Algebra 线性代数"],
                ["Theory Of Matrix 矩阵理论"],
                ["Theory Of Probability 概率论"],
                ["Statistics 统计"],
                ["Differential Equation 微分方程"],
                ["Physics 物理"]
            ],
            columns=["Mathematics & Physics 数理类"]
        )
    )
    st.markdown("#### 🛠️工科类")
    st.table(
        pd.DataFrame(
            [
                ["Theory Of Control 控制理论"],
                ["Theory Of Linear System 线性系统理论"],
                ["Numerical Method 数值方法"]
            ],
            columns=["Engineering 工科类"]
        )
    )
    st.markdown("#### ⌨️编程类")
    st.table(
        pd.DataFrame(
            [
                ["Matlab", "Matlab"],
                ["Java", "Java"],
                ["Python", "Python"],
                ["Data Structure", "数据结构"],
                ["Algorithm", "算法"]
            ],
            columns=["Programming", "编程类"],
            index=None
        ),
    )



