# dashboard/soc_dashboard.py

import streamlit as st


def soc_dashboard():

    st.title(
        "🛡 Security Operations Center"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Critical Threats",
        0
    )

    col2.metric(
        "High Threats",
        0
    )

    col3.metric(
        "Medium Threats",
        0
    )

    st.info(
        "SOC Dashboard Active"
    )