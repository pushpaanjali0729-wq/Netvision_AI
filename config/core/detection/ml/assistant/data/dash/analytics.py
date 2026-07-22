# dashboard/analytics.py

import streamlit as st


def analytics_panel(df):

    st.subheader(
        "📊 Traffic Analytics"
    )

    st.write(
        f"Total Records: {len(df)}"
    )

    if "packet_length" in df.columns:

        st.write(

            f"Average Size: "

            f"{df['packet_length'].mean():.2f}"
        )