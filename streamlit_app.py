
import streamlit as st


st.write("Καλώς ήρθες ...")



pg = st.navigation([st.Page("pages/page_01.py"), st.Page("pages/page_02.py")])
pg.run()