import os.path

from common.path_handler import path_handler
import streamlit as st


if __name__ == "__main__":
    st.set_page_config(page_title="辅导经验 留学课程作业考试辅导答疑家教 个人老师", page_icon="🧑‍🏫")
    st.sidebar.image(path_handler.profile_file_path)
    st.title("辅导经验")
    column_1, column_2, column_3 = st.columns(3)
    column_1.metric(label="辅导人次", value="300人+", delta="值得信赖", delta_color="normal")
    column_2.metric(label="辅导生涯", value="4年+", delta="经验丰富", delta_color="normal")
    column_3.metric(label="好评比例", value="100%", delta="保证质量", delta_color="normal")
    st.markdown("###")
    st.markdown("### 👨‍🔬自我陈述")
    st.markdown("从2020年读研开始接触留学生辅导这块的内容，刚开始是和辅导机构和中介合作，基本上是有什么做什么，生源是机构中介的生源，没有接触的机会，也没想那么多。")
    st.markdown("一次偶然的机会，接触到了一个学生，在和他沟通之后得知中介的抽成比例居然高达90%的时候，我震惊了，利用老师-学生两端信息的不对等，不学无术的机构和中介吃得满嘴流油，无形中提高了学生的教育成本，侵占了老师的劳动成果。")
    st.markdown("后来，了解到了更多的信息，网上一堆针对留学生的辅导机构，搭建网页，开设店铺，对外宣称拥有来自于海外常青藤高校联盟、国内清北复交的硕博教师团队，实际上只是不负责任的外包中间人，招聘教师的质量良莠不齐，更有甚者，会将所有有意接单的人拉到派单群里，接到了学生的辅导请求只是简单往群里一扔，有没有能力满足学生的辅导需求从来不是他们所关心的，糊弄完事便万事大吉。")
    st.markdown("看清楚机构中介的嘴脸，想明白个中的弯弯绕绕，便终止了和机构中介的虚与委蛇，这帮人让我恶心。。。")
    st.markdown("再往后，个人开了一家闲鱼店铺（闲鱼号: NightFall），拥有了直接和学生生源对接的机会，帮助了上百位留学生，累计辅导人次300+，在这个过程中，接的单子都是自己学过并且确有把握的，手写和电子文档均可，也有学生拿着我不懂的科目过来咨询，都被我回绝了，不会就是不会，也不想去找外包————既然讨厌这种人，便不想成为这种人。")
    st.markdown("如果屏幕前的你刚好有课业辅导的需求，可以尝试联系我，会与不会我都直说，会的话我们可以商量出一个双方都满意的价格，不会的话也不会耽误你的时间。如果确有合作的意向，也不用担心资金的安全，我们可以走闲鱼平台，合作结束、结果满意的话再确认收货，双方都安全。")
    st.markdown("最后一句话：你不主动，故事便不会开始~")
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
    for file_name in sorted(os.listdir(path_handler.works_folder_path), reverse=True):
        column_1, column_2 = st.columns([8, 1], vertical_alignment="center")
        column_1.markdown(file_name.replace("_", " "))
        with open(os.path.join(path_handler.works_folder_path, file_name), mode="rb") as file:
            column_2.download_button(label="下载", data=file, file_name=file_name.replace("_", " "))
