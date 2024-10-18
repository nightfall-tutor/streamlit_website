from lib.basic_functions import get_database_connector
from common.secret_handler import secret_handler
import streamlit as st


if __name__ == "__main__":
    secret_handler.db_host = st.secrets["db_host"]
    secret_handler.db_username = st.secrets["db_username"]
    secret_handler.db_password = st.secrets["db_password"]
    secret_handler.db_database = st.secrets["db_database"]
    database_connector = get_database_connector()
    # database_connector.force_commit()
    database_connector.reset_table_streamlit_website_statistics()
    database_connector.reset_table_streamlit_website_visitors()
    database_connector.reset_table_streamlit_website_clickers()
    database_connector.reset_table_streamlit_website_contacts()

