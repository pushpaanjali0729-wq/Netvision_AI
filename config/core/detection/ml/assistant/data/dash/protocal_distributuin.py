# dashboard/protocol_distribution.py

import plotly.express as px
import streamlit as st


def protocol_distribution(df):

    if "protocol" not in df.columns:
        return

    protocol_counts = (

        df["protocol"]

        .value_counts()

        .reset_index()
    )

    protocol_counts.columns = [

        "Protocol",

        "Count"
    ]

    fig = px.bar(

        protocol_counts,

        x="Protocol",

        y="Count",

        title="Protocol Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )