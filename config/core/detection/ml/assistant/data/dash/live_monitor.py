# dashboard/live_monitor.py

import streamlit as st


def live_monitor(
        packets,
        bandwidth
):

    st.subheader(
        "📡 Live Monitor"
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Packets/sec",
        packets
    )

    col2.metric(
        "Bandwidth",
        f"{bandwidth} MB"
    )