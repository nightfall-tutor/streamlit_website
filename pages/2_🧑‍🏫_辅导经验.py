import os.path

from common.path_handler import path_handler
import streamlit as st


if __name__ == "__main__":
    st.sidebar.image(path_handler.profile_file_path)
    st.title("辅导经验")
    # st.markdown("###")
    # st.markdown("### 👨‍🔬总结一览")
    column_1, column_2, column_3 = st.columns(3)
    column_1.metric(label="辅导人次", value="300人+", delta="值得信赖", delta_color="normal")
    column_2.metric(label="辅导生涯", value="4年+", delta="经验丰富", delta_color="normal")
    column_3.metric(label="好评比例", value="100%", delta="保证质量", delta_color="normal")
    st.markdown("###")
    st.markdown("### 👨‍🔬自我陈述")
    st.markdown("###")
    st.markdown("### 💬学生评价")
    column_1, column_2, column_3, column_4, column_5, column_6 = st.columns(6)
    for index in range(0, 3):
        column_1.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 1}.jpg"))
        column_2.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 2}.jpg"))
        column_3.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 3}.jpg"))
        column_4.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 4}.jpg"))
        column_5.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 5}.jpg"))
        column_6.image(os.path.join(path_handler.comments_folder_path, f"comment_{6 * index + 6}.jpg"))
    st.markdown("###")
    st.markdown("### 📃过往作品")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20240210 Assignment to Physics.pdf")
    with open(os.path.join(path_handler.works_folder_path, "20240210_Assignment_to_Physics.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20240210 Assignment to Physics.pdf")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20240102 Assignment to Statistics.pdf")
    with open(os.path.join(path_handler.works_folder_path, "20240102_Assignment_to_Statistics.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20240102 Assignment to Statistics.pdf")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20231230 Report to Lab Electronics.pdf")
    with open(os.path.join(path_handler.works_folder_path, "20231230_Report_to_Lab_Electronics.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20231230 Report to Lab Electronics.pdf")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20231002 Assignment to Matlab.pdf")
    with open(os.path.join(path_handler.works_folder_path, "20231002_Assignment_to_Matlab.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20231002 Assignment to Matlab.pdf")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20230914 Assignment to Matrix Theory.pdf")
    with open(os.path.join(path_handler.works_folder_path, "20230914_Assignment_to_Matrix_Theory.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20230914 Assignment to Matrix Theory.pdf")
    column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
    column_1.markdown("20230906 Assignment to Mathematics")
    with open(os.path.join(path_handler.works_folder_path, "20230906_Assignment_to_Mathematics.pdf"), mode="rb") as file:
        column_2.download_button(label="下载", data=file, file_name="20230906 Assignment to Mathematics")
