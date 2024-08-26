from lib.cached_functions import get_random_seed
import streamlit as st


if __name__ == "__main__":
    st.title("优势介绍")
    if st.button("点击获取随机种子："):
        st.write(get_random_seed())


