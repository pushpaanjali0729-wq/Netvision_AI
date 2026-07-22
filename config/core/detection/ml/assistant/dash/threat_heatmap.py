# dashboard/threat_heatmap.py

import streamlit as st
import plotly.express as px


def threat_heatmap(df):

    if (
        "src_ip" not in df.columns or
        "dst_ip" not in df.columns
    ):
        return

    heatmap = (
        df.groupby(
            ["src_ip", "dst_ip"]
        )
        .size()
        .reset_index(name="count")
    )

    fig = px.density_heatmap(

        heatmap,

        x="src_ip",

        y="dst_ip",

        z="count",

        title="Threat Heatmap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )