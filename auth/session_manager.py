import streamlit as st


def create_session(user):

    st.session_state["user"] = user


def logout():

    if "user" in st.session_state:
        del st.session_state["user"]


def is_logged_in():

    return "user" in st.session_state
