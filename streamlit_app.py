
import streamlit as st


st.write("Καλώς ήρθες ...")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page("pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True)
page_01 = st.Page("pages/page_01.py", title="page 1", icon=":material/bug_report:")
page_02 = st.Page("pages/page_02.py", title="page 2", icon=":material/notification_important:")

search = st.Page("pages/search.py", title="Search", icon=":material/search:")
history = st.Page("pages/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Pages": [dashboard, page_01, page_02],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()