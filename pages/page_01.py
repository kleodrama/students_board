
import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

worksheet_classes = "1787667360"
worksheet_students = "1985906332"
worksheet_dokimasies = "843658394"
worksheet_apotelesmata_dokimasias = "606650409"

# Σχολεία
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()

# Τάξεις
df_classes = conn.read(worksheet=worksheet_classes)

# Μαθητές
df_students = conn.read(worksheet=worksheet_students)

# Λίστα με τα σχολεία
l_0 = list(df.iloc[::-1].itertuples(index=False))
options = list()
for i in l_0:
    options.append(f"{i[0]} - {i[1]} ({i[2]})")

school = st.selectbox(
    "Σχολείο",
    options,
)
school_id = school[0]
# st.write("You selected school with id:", school_id)

# Λίστα με τις τάξεις
sql = f'select * from "classes" WHERE school_id={school_id}'
df_temp = conn.query(worksheet=worksheet_classes, sql=sql, ttl=3600)
# st.write(df_temp)

l_1 = list(df_temp.iloc[::-1].itertuples(index=False))
options_classes = list()
for i in l_1:
    options_classes.append(f"{i[0]} - {i[1]} ({i[2]})")

selected_class = st.selectbox(
    "Τμήμα",
    options_classes,
)
selected_class_id = selected_class[0]
# st.write("You selected class with id:", selected_class_id)






tab1, tab2, tab3 = st.tabs(["Α Τετράμηνο", "Β Τετράμηνο", "Εξετάσεις"])
with tab1:
    # Πίνακας με τους μαθητές
    sql_2 = f'select * from "students" WHERE class_id={selected_class_id}'
    df_temp_2 = conn.query(worksheet=worksheet_students, sql=sql_2, ttl=3600)

    st.write(df_temp_2)

    # Ανάκτηση όλων των δοκιμασιών για το τμήμα
    # Πίνακας με τις δοκιμασίες του τμήματος
    sql_3 = f'select * from "dokimasies" WHERE class_id={selected_class_id}'
    df_temp_3 = conn.query(worksheet=worksheet_dokimasies, sql=sql_3, ttl=3600)

    # Όλα τα αποτελέσματα δοκιμασιών για τις δοκιμασίες του τμήματος
    st.write(df_temp_3)
    list_dokimasies = list()
    for i in df_temp_3.itertuples():
        list_dokimasies.append(i.id)
    if len(list_dokimasies) > 0:
        sql_apotelesmata_dokimasion = f'SELECT * FROM apotelesmata_dokimasias WHERE dokimasia_id IN {list_dokimasies}'
        df_temp_apotelesmata_dokimasion = conn.query(worksheet=worksheet_apotelesmata_dokimasias, sql=sql_apotelesmata_dokimasion, ttl=3600)
        # st.write(df_temp_apotelesmata_dokimasion)
    else:
        df_temp_apotelesmata_dokimasion = None
        st.write("Δεν υπάρχουν δοκιμασίες για υτό το τμήμα.")
with tab2:
    st.header("Λίστα με βαθμούς κλπ κλπ")

    titles = list()
    titles.append('id')
    titles.append('Επώνυμο')
    titles.append('Όνομα')
    for i in df_temp_3.itertuples():
        titles.append(i.name)

    # loop στους μαθητές
    eponima = list()
    names = list()

    list_mathites = list()

    if df_temp_apotelesmata_dokimasion is not None:
        dataframe_apotelesmata_dokimasion = pd.DataFrame(df_temp_apotelesmata_dokimasion, columns=['id', 'student_id', 'dokimasia_id', 'vathmos'])
    else:
        dataframe_apotelesmata_dokimasion = None
    apotelesmata_dokimasion = list()
    for row in df_temp_2.itertuples():

        list_mathiti = list()
        list_mathiti.append(row.id)
        list_mathiti.append(row.surname)
        list_mathiti.append(row.name)

        # loop στις δοκιμασιες
        for i in df_temp_3.itertuples():
            apotelesma = dataframe_apotelesmata_dokimasion.query(f'dokimasia_id=={i.id} and student_id=={row.id}')["vathmos"]
            if apotelesma.empty:
                list_mathiti.append(None)
            else:
                list_mathiti.append(apotelesma.to_numpy())

        list_mathites.append(list_mathiti)

    dataframe_mathites = pd.DataFrame(list_mathites, columns = titles)
    st.write(dataframe_mathites)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)











