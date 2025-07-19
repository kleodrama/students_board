
import streamlit as st
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

worksheet_classes = "1787667360"
df_classes = conn.read(worksheet=worksheet_classes)

for row in df.iloc[::-1].itertuples():
    with st.expander(f"({row.season}): {row.name}", expanded=False, icon=None, width="stretch"):
        st.write(f"({row.season}): {row.name}")
        st.write(f"id ---> {row.school_id}")
        sql = f'select * from "classes" WHERE school_id={row.school_id}'
        df_temp = conn.query(worksheet=worksheet_classes, sql=sql, ttl=3600)
        for row_2 in df_temp.itertuples():
            # st.write(df_temp)
            st.page_link(f"http://localhost:8501/?class={row_2.class_id}", label=row_2.name)
            # if st.button(row_2.name, key=f"{row.season}-{row_2.name}"):
            #     # if 'user_select_value' not in st.session_state:
            #     #     st.session_state['user_select_value'] = 0  # or whatever default
            #     # user_select_value = st.session_state['user_select_value']
            #     st.navigate("page_01")

# Second Sheet ---> classes
for row in df_classes.itertuples():
    st.write(f"({row.name})")

with st.expander("Σχολείο 1", expanded=False, icon=None, width="stretch"):
    "Εδώ θα εμφανίζονται τα τμήματα του σχολείου 1"
    st.button("α1")
    st.button("Γ1")
    st.button("β4")
    with st.popover("Προσθήκη τμήματος"):
        st.markdown("Στοιχεία τμήματος 👋")
        st.text_input("Όνομα τμήματος (π.χ. A1)")
        st.selectbox("Τάξη",
                       ("α γυμνασίου", "β γυμνασίου", "γ γυμνασίου",
                        "Α λυκείου", "Β λυκείου", "Γ λυκείου",
                        "Α ΕΠΑΛ", "Β ΕΠΑΛ", "Γ ΕΠΑΛ",),)
        st.button("Προσθήκη")

with st.expander("Σχολείο 2", expanded=False, icon=None, width="stretch"):
    "Εδώ θα εμφανίζονται τα τμήματα του σχολείου 2"
    st.button("γ1")
    # st.button("Γ1")
    st.button("γ4")
    with st.popover("Προσθήκη τμήματος"):
        st.markdown("Στοιχεία τμήματος 👋")
        st.text_input("Όνομα τμήματος (π.χ. A2)")
        st.selectbox("Τάξη2",
                       ("α γυμνασίου", "β γυμνασίου", "γ γυμνασίου",
                        "Α λυκείου", "Β λυκείου", "Γ λυκείου",
                        "Α ΕΠΑΛ", "Β ΕΠΑΛ", "Γ ΕΠΑΛ",),)
        st.button("Προσθήκη2")

