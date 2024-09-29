from common.path_handler import path_handler
import os


if __name__ == "__main__":
    print(os.path.join(path_handler.works_folder_path, "20240210_Assignment_to_Physics.pdf"))
    print(os.path.exists(os.path.join(path_handler.works_folder_path, "20240210_Assignment_to_Physics.pdf")))
