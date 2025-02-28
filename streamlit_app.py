import streamlit as st
import pandas as pd


st.title("Titanic Data Dashboard")


df = pd.read_csv('data/titanic_data.csv')


st.write("### Titanic Dataset Preview:")
st.dataframe(df.head())


st.write("### Survival Count")
survivors = df[df["Survived"] == 1]
survivor_counts = survivors["Sex"].value_counts()
st.bar_chart(survivor_counts, use_container_width = False, width=200)


gender = st.selectbox("Select Gender", df["Sex"].unique())
filtered_data = df[df["Sex"] == gender]
st.write("### Filtered Data by Gender:")
st.dataframe(filtered_data)


with st.container():
    st.write("### Additional Info")
    st.write(f"Total Passengers: {len(df)}")
    st.write(f"Survival Rate: {df['Survived'].mean()*100:.2f}%")
