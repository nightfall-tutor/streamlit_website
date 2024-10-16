from common.logger import logger
import mysql.connector


class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connector = None
        self.cursor = None
        self.init_connection()

    def init_connection(self):
        for attempt in range(1, 4):
            try:
                self.connector = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    passwd=self.password,
                    database=self.database
                )
                self.cursor = self.connector.cursor()
                logger.debug(f"Succeed to connect to MySQL database (attempt {attempt})")
                self.cursor.execute("select * from streamlit_website_statistics")
                if not self.cursor.fetchall():
                    self.cursor.execute("insert into streamlit_website_statistics (id, visitor_count, clicker_count) values (1, 0, 0)")  # 初始化streamlit_website_statistics表格
                    self.connector.commit()
                break
            except Exception as ex:
                self.connector = None
                self.cursor = None
                logger.error(f"Fail to connect to MySQL database due to {ex} (attempt {attempt})")

    def reset_table_streamlit_website_statistics(self):
        self.cursor.execute("delete from streamlit_website_statistics")
        self.cursor.execute("insert into streamlit_website_statistics (id, visitor_count, clicker_count) values (1, 0, 0)")
        self.connector.commit()

    def get_visitor_count(self):
        self.cursor.execute("select visitor_count from streamlit_website_statistics where id = 1")
        return self.cursor.fetchone()[0]

    def update_visitor_count(self):
        self.cursor.execute(f"update streamlit_website_statistics set visitor_count = {self.get_visitor_count() + 1} where id = 1")
        self.connector.commit()

    def get_clicker_count(self):
        self.cursor.execute("select clicker_count from streamlit_website_statistics where id = 1")
        return self.cursor.fetchone()[0]

    def update_clicker_count(self):
        self.cursor.execute(f"update streamlit_website_statistics set clicker_count = {self.get_clicker_count() + 1} where id = 1")
        self.connector.commit()

    def update_contact_information(self, platform, contact_information):
        self.cursor.execute(f"insert into streamlit_website_contacts (platform, contact_information) values ({platform}, {contact_information})")
        self.connector.commit()





