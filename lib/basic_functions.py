from common.database_connector import DatabaseConnector
from common.logger import logger
import streamlit as st
import datetime
import uuid
import time


@st.cache_data
def get_random_seed():  # 基于uuid全局标识符和当前时间戳生成随机种子
    return uuid.uuid4()


@st.cache_resource
def get_database_connector(host, user, password, database):
    logger.debug("Get singleton of database connector")
    return DatabaseConnector(host, user, password, database)


@st.cache_data
def update_visitor_count(parameters):
    logger.debug("Update visitor count")
    get_database_connector(parameters[0], parameters[1], parameters[2], parameters[3]).update_visitor_count()


@st.cache_data
def update_clicker_count(parameters):
    logger.debug("Update clicker count")
    get_database_connector(parameters[0], parameters[1], parameters[2], parameters[3]).update_clicker_count()


@st.cache_data
def update_contact_information(parameters, platform, contact_information):
    logger.debug("Update contact information")
    get_database_connector(parameters[0], parameters[1], parameters[2], parameters[3]).update_contact_information(platform, contact_information)






