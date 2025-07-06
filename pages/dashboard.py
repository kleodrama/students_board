
import streamlit as st
from streamlit_gsheets import GSheetsConnection


conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
for row in df.itertuples():
    with st.expander(f"({row.season}): {row.name}", expanded=False, icon=None, width="stretch"):
        st.write(f"({row.season}): {row.name}")
        st.write(f"id ---> {row.school_id}")


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

