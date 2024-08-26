import os.path
import streamlit as st
from lib.data_handler import DataHandler


if __name__ == "__main__":
    st.title("联系方式")
    container_get_contact_information = st.empty()  # 使用容器实现按钮消失
    button_get_contact_information = container_get_contact_information.button("点击获取联系方式")
    if button_get_contact_information:
        DataHandler.get_data_handler_singleton().update_number_clicker()
        container_get_contact_information.empty()
        st.header("微信ID：")
        st.write("IdeaBeneathMask")
        st.header("微信QR：")
        st.image(os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "Wechat_QR.jpg"))
        st.header("邮箱：")
        st.write("nightfall1998@163.com")
