# dashboard/network_health.py

import streamlit as st


def network_health(
        anomalies,
        threats
):

    score = 100

    score -= anomalies * 2

    score -= threats * 3

    score = max(score, 0)

    st.metric(
        "Network Health",
        f"{score}%"
    )

    if score > 80:

        st.success(
            "Healthy"
        )

    elif score > 50:

        st.warning(
            "Warning"
        )

    else:

        st.error(
            "Critical"
        )