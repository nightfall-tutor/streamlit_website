from common.path_handler import path_handler
import json


class DataHandler:
    def __init__(self):
        self.data_path = path_handler.data_file_path
        self.data = None
        self.get_data()

    def get_data(self):
        with open(self.data_path, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)
        return self.data

    def update_data(self):
        with open(self.data_path, mode="w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def get_visitor_count(self):
        return self.data["visitor count"]

    def update_visitor_count(self):
        self.data["visitor count"] += 1
        self.update_data()

    def get_clicker_count(self):
        return self.data["clicker count"]

    def update_clicker_count(self):
        self.data["clicker count"] += 1
        self.update_data()

    def get_contact_information(self):
        return self.data["contact information"]

    def update_contact_information(self, new_contact_information: str):
        self.data["contact information"].append(new_contact_information)
        self.update_data()


data_handler = DataHandler()
