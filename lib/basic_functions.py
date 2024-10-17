from common.database_connector import DatabaseConnector
from common.secret_handler import secret_handler
from common.logger import logger
import streamlit as st
import uuid


@st.cache_data
def get_uuid():
    result = uuid.uuid4()
    logger.debug(f"Get uuid as {result}")
    return result


@st.cache_resource
def get_database_connector():
    logger.debug("Get singleton of database connector")
    return DatabaseConnector(
        host=secret_handler.db_host,
        user=secret_handler.db_username,
        password=secret_handler.db_password,
        database=secret_handler.db_database
    )


@st.cache_data
def update_visitor_information():
    logger.debug("Update visitor information")
    database_connector = get_database_connector()
    database_connector.update_visitor_information(get_uuid())


@st.cache_data
def update_clicker_information():
    logger.debug("Update clicker information")
    database_connector = get_database_connector()
    database_connector.update_clicker_information(get_uuid())


@st.cache_data
def update_contact_information(platform, contact_information):
    logger.debug("Update contact information")
    database_connector = get_database_connector()
    database_connector.update_contact_information(platform, contact_information)

