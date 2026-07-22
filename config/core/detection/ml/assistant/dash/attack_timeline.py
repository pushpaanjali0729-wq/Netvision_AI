# dashboard/attack_timeline.py

import plotly.express as px
import streamlit as st


def attack_timeline(df):

    if "timestamp" not in df.columns:
        return

    timeline = (
        df.groupby("timestamp")
        .size()
        .reset_index(name="count")
    )

    fig = px.line(
        timeline,
        x="timestamp",
        y="count",
        title="Attack Timeline"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )