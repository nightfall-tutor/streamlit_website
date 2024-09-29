import os


class PathHandler:
    def __init__(self):
        self.root_folder_path = os.path.dirname(os.path.dirname(__file__))
        self.log_file_path = os.path.join(self.root_folder_path, "log", "log.log")
        self.data_file_path = os.path.join(self.root_folder_path, "data", "data.json")
        self.profile_file_path = os.path.join(self.root_folder_path, "resources", "profile.jpg")
        self.wechat_qr_file_path = os.path.join(self.root_folder_path, "resources", "wechat_qr.jpg")
        self.comments_folder_path = os.path.join(self.root_folder_path, "resources", "comments")


path_handler = PathHandler()
