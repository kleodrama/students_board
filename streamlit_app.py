
import streamlit as st


# st.write("Καλώς ήρθες ...")
st.set_page_config(layout="wide")

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

def logout_screen():
    st.button("Log out", on_click=st.logout)


if (not st.user) or (not st.user.is_logged_in):

    ##########################
    # st.session_state.logged_in = False
    ##########################

    # login_screen()

    st.badge("fake user!!", icon=":material/check:", color="green")
    st.session_state.logged_in = True

else:
    st.badge(st.user.given_name, icon=":material/check:", color="green")
    st.session_state.logged_in = True

# st.write(st.session_state)


login_page = st.Page(login_screen, title="Log in", icon=":material/login:")
logout_page = st.Page(logout_screen, title="Log out", icon=":material/logout:")

dashboard = st.Page("pages/dashboard.py", title="Σχολεία", icon=":material/dashboard:", default=True)
page_01 = st.Page("pages/page_01.py", title="Πίνακας", icon=":material/bug_report:")
page_02 = st.Page("pages/page_02.py", title="page 2", icon=":material/notification_important:")

school = st.Page("pages/search.py", title="Σχολείο", icon=":material/search:")
_class = st.Page("pages/history.py", title="Τμήμα", icon=":material/history:")
student = st.Page("pages/student.py", title="Μαθητής", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Λογαριασμός": [logout_page],
            "Σελίδες": [dashboard, page_01, page_02],
            "Προσθήκη": [school, _class, student],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()