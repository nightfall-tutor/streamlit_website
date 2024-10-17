import os


class PathHandler:
    def __init__(self):
        self.root_folder_path = os.path.dirname(os.path.dirname(__file__))
        self.resources_folder_path = os.path.join(self.root_folder_path, "resources")
        self.profile_file_path = os.path.join(self.root_folder_path, "resources", "profile.jpg")
        self.wechat_qr_file_path = os.path.join(self.root_folder_path, "resources", "wechat_qr.jpg")
        self.comments_folder_path = os.path.join(self.root_folder_path, "resources", "comments")
        self.works_folder_path = os.path.join(self.root_folder_path, "resources", "works")


path_handler = PathHandler()
