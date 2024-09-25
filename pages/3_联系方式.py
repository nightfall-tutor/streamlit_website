import os.path
import streamlit as st
from lib.basic_functions import update_clicker_count, update_contact_information
from common.path_handler import path_handler


if __name__ == "__main__":
    st.title("联系方式")

    st.markdown("### 📧留下你的联系方式")
    st.markdown("#### 📱社交平台")
    select_box_social_platform = st.selectbox(label="选择社交平台",
                                              options=["微信", "QQ", "邮箱"],
                                              index=None if "social platform" not in st.session_state else ["微信", "QQ", "邮箱"].index(st.session_state["social platform"]))
    st.markdown("#### 📞联系方式")
    text_input_contact_information = st.text_input(label="输入联系方式", value="" if "contact information" not in st.session_state else st.session_state["contact information"])
    button_confirm = st.button("确认")
    if button_confirm:
        if not select_box_social_platform:
            st.markdown('<p style="color: red;">请选择社交平台</p>', unsafe_allow_html=True)
        elif not text_input_contact_information:
            st.markdown('<p style="color: red;">请输入联系方式</p>', unsafe_allow_html=True)
        else:
            st.session_state["social platform"] = select_box_social_platform
            st.session_state["contact information"] = text_input_contact_information
            update_contact_information(f"{st.session_state['social platform']} - {st.session_state['contact information']}")
            st.markdown('<p style="color: green;">保存成功</p>', unsafe_allow_html=True)

    st.markdown("### 🧑‍💻获取我的联系方式")
    container_get_contact_information = st.empty()  # 使用容器实现按钮消失
    button_get_contact_information = container_get_contact_information.button("获取")
    if button_get_contact_information or "is contact information showed" in st.session_state:
        update_clicker_count()
        st.session_state["is contact information showed"] = True
        container_get_contact_information.empty()
        st.markdown("#### 📲微信ID")
        st.markdown("**IdeaBeneathMask**")
        st.markdown("#### 🪪微信QR")
        st.image(path_handler.wechat_qr_file_path)
        st.markdown("#### 📮邮箱地址")
        st.markdown("**nightfall1998@163.com**")
