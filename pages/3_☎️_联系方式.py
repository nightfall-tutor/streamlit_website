from lib.basic_functions import update_clicker_information, update_contact_information, get_email_notifier
from common.path_handler import path_handler
import streamlit as st


if __name__ == "__main__":
    st.set_page_config(page_title="联系方式 留学课程作业考试辅导答疑家教 个人老师", page_icon="☎️")
    st.title("联系方式")
    st.sidebar.image(path_handler.profile_file_path)
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
            st.error("请选择社交平台", icon="❎")
        elif not text_input_contact_information:
            st.error("请输入联系方式", icon="❎")
        else:
            st.session_state["social platform"] = select_box_social_platform
            st.session_state["contact information"] = text_input_contact_information
            update_contact_information(platform=st.session_state['social platform'], contact_information=st.session_state['contact information'])
            get_email_notifier().send_email(subject="New contact information has been submitted", message=f"Social platform: {select_box_social_platform}\n"
                                                                                                          f"Contact information: {text_input_contact_information}")
            st.success("保存成功", icon="✅")
    st.markdown("###")
    st.markdown("### 🧑‍💻获取我的联系方式")
    container_get_contact_information = st.empty()  # 使用容器实现按钮消失
    button_get_contact_information = container_get_contact_information.button("获取")
    if button_get_contact_information or "is contact information showed" in st.session_state:
        if "is contact information showed" not in st.session_state:
            st.session_state["is contact information showed"] = True
            update_clicker_information()
        container_get_contact_information.empty()
        st.markdown("#### 📲微信ID")
        st.markdown("**IdeaBeneathMask**")
        st.markdown("#### 🪪微信QR")
        st.image(path_handler.wechat_qr_file_path)
        st.markdown("#### 📮邮箱地址")
        st.markdown("**nightfall1998@163.com**")
