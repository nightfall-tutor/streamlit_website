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
                self.cursor.execute("select count(*) as row_count from streamlit_website_statistics")
                row_count = self.cursor.fetchone()
                if row_count and row_count[0] == 0:
                    self.cursor.execute("insert into streamlit_website_statistics (id, visitor_count, clicker_count, contact_count) values (1, 0, 0, 0)")  # 初始化streamlit_website_statistics表格
                    self.connector.commit()
                break
            except Exception as ex:
                self.connector = None
                self.cursor = None
                logger.error(f"Fail to connect to MySQL database due to {ex} (attempt {attempt})")

    def force_commit(self):
        self.connector.commit()

    def reset_table_streamlit_website_statistics(self):
        try:
            self.cursor.execute("delete from streamlit_website_statistics")
            self.cursor.execute("insert into streamlit_website_statistics (id, visitor_count, clicker_count, contact_count) values (1, 0, 0, 0)")
            self.connector.commit()
            logger.debug("Succeed to reset table streamlit_website_statistics")
        except Exception as ex:
            logger.error(f"Fail to reset table streamlit_website_statistics due to {ex}")

    def reset_table_streamlit_website_visitors(self):
        try:
            self.cursor.execute("truncate table streamlit_website_visitors")
            self.connector.commit()
            logger.debug("Succeed to reset table streamlit_website_visitors")
        except Exception as ex:
            logger.error(f"Fail to reset table streamlit_website_visitors due to {ex}")

    def reset_table_streamlit_website_clickers(self):
        try:
            self.cursor.execute("truncate table streamlit_website_clickers")
            self.connector.commit()
            logger.debug("Succeed to reset table streamlit_website_clickers")
        except Exception as ex:
            logger.error(f"Fail to reset table streamlit_website_clickers due to {ex}")

    def reset_table_streamlit_website_contacts(self):
        try:
            self.cursor.execute("truncate table streamlit_website_contacts")
            self.connector.commit()
            logger.debug("Succeed to reset table streamlit_website_contacts")
        except Exception as ex:
            logger.error(f"Fail to reset table streamlit_website_contacts due to {ex}")

    def get_visitor_count(self):
        self.cursor.execute("select visitor_count from streamlit_website_statistics where id = 1")
        visitor_count = self.cursor.fetchone()[0]
        logger.debug(f"Succeed to get visitor count as {visitor_count}")
        return visitor_count

    def update_visitor_information(self):
        try:
            self.cursor.execute(f"update streamlit_website_statistics set visitor_count = {self.get_visitor_count() + 1} where id = 1")
            self.cursor.execute(f"insert into streamlit_website_visitors () values ()")
            self.connector.commit()
            logger.debug("Succeed to update visitor information")
        except Exception as ex:
            logger.error(f"Fail to update visitor information due to {ex}")

    def get_clicker_count(self):
        self.cursor.execute("select clicker_count from streamlit_website_statistics where id = 1")
        clicker_count = self.cursor.fetchone()[0]
        logger.debug(f"Succeed to get clicker count as {clicker_count}")
        return clicker_count

    def update_clicker_information(self):
        try:
            self.cursor.execute(f"update streamlit_website_statistics set clicker_count = {self.get_clicker_count() + 1} where id = 1")
            self.cursor.execute(f"insert into streamlit_website_clickers () values ()")
            self.connector.commit()
            logger.debug("Succeed to update clicker information")
        except Exception as ex:
            logger.error(f"Fail to update clicker information due to {ex}")

    def get_contact_count(self):
        self.cursor.execute("select contact_count from streamlit_website_statistics where id = 1")
        contact_count = self.cursor.fetchone()[0]
        logger.debug(f"Succeed to get clicker count as {contact_count}")
        return contact_count

    def update_contact_information(self, platform, contact_information):
        try:
            self.cursor.execute(f"update streamlit_website_statistics set contact_count = {self.get_contact_count() + 1} where id = 1")
            self.cursor.execute(f"insert into streamlit_website_contacts (platform, contact_information) values ('{platform}', '{contact_information}')")
            self.connector.commit()
            logger.debug(f"Succeed to update contact information (platform={platform}, contact_information={contact_information})")
        except Exception as ex:
            logger.debug(f"Fail to update contact information (platform={platform}, contact_information={contact_information}) due to {ex}")





