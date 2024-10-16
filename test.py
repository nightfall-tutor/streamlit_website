from common.database_connector import DatabaseConnector
import streamlit as st


if __name__ == "__main__":
    database_connector = DatabaseConnector(
        host=st.secrets["db_host"],
        user=st.secrets["db_username"],
        password=st.secrets["db_password"],
        database=st.secrets["db_database"]
    )
    database_connector.reset_table_streamlit_website_statistics()
    # print(database_connector.get_visitor_count())
    # database_connector.update_visitor_count()
    # print(database_connector.get_visitor_count())
    # database_connector.execute("DELETE FROM streamlit_website_statistics")
    # database_connector.execute("INSERT INTO streamlit_website_statistics (visitor_count, clicker_count) VALUES (0, 0)")

