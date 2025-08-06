
import streamlit as st
from streamlit_gsheets import GSheetsConnection
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

# Πίνακας με τους μαθητές
sql_2 = f'select * from "students" WHERE class_id={selected_class_id}'
df_temp_2 = conn.query(worksheet=worksheet_students, sql=sql_2, ttl=3600)

st.write(df_temp_2)

# Πίνακας με τις δοκιμασίες της τάξης
sql_3 = f'select * from "dokimasies" WHERE class_id={selected_class_id}'
df_temp_3 = conn.query(worksheet=worksheet_dokimasies, sql=sql_3, ttl=3600)

st.write(df_temp_3)


# Αποτελέσματα δοκιμασίας για κάθε μαθητή

# loop στους μαθητές
for row in df_temp_2.itertuples():
    st.write(f"Ο μαθητής {row.name} έγραψε τις παρακάτω δοκιμασίες")
    # loop στις δοκιμασίες
    for row_2 in df_temp_3.itertuples():
        sql_temp = f'select * from "apotelesmata_dokimasias" WHERE student_id={row.id} and dokimasia_id={row_2.id}'
        df_temp_4 = conn.query(worksheet=worksheet_apotelesmata_dokimasias, sql=sql_temp, ttl=3600)
        # st.write(df_temp_4)
        # loop στα αποτελέσματα δοκιμασιών
        for row_3 in df_temp_4.itertuples():
            st.write(f"{row_2.name} --> {row_3.vathmos} στα {row_2.arista}")








