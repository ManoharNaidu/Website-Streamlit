import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Sample Data Dashboard")
upload_file = st.file_uploader("Upload-File", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    # preview
    st.subheader("Data Preview")
    st.write(df.head())

    # summary
    st.subheader("Data Summary")
    st.write(df.describe())

    # filtering
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select Column to filter",columns)

    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting you to upload the file...:)")


# streamlit run main.py - to run the server