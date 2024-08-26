import json
import os.path


class DataHandler:
    data_handler_singleton = None

    @staticmethod
    def get_data_handler_singleton():
        if not DataHandler.data_handler_singleton:
            DataHandler.data_handler_singleton = DataHandler()
        return DataHandler.data_handler_singleton

    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "data.json")
        self.data = None
        self.read_data()

    def read_data(self):
        with open(self.data_path, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    def write_data(self):
        with open(self.data_path, mode="w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def update_number_clicker(self):
        self.data["number_clicker"] += 1
        self.write_data()


if __name__ == "__main__":
    data_handler = DataHandler.get_data_handler_singleton()
    print(data_handler.data)
