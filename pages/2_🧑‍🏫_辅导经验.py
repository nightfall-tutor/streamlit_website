from common.path_handler import path_handler
import streamlit as st


if __name__ == "__main__":
    st.sidebar.image(path_handler.profile_file_path)
    st.title("辅导经验")
