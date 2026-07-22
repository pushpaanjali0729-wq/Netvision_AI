# app.py

import sqlite3
import pandas as pd
import streamlit as st

from dashboard.kpi import display_kpis
from dashboard.charts import (
    protocol_chart,
    packet_size_chart
)

from dashboard.insights import (
    generate_insights
)

from dashboard.top_talkers import (
    show_top_talkers
)

from dashboard.protocol_distribution import (
    protocol_distribution
)

from dashboard.network_health import (
    network_health
)

from dashboard.attack_timeline import (
    attack_timeline
)

from dashboard.threat_heatmap import (
    threat_heatmap
)

from dashboard.soc_dashboard import (
    soc_dashboard
)

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="NetVision AI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------

def load_css():

    try:

        with open(
            "assets/styles.css",
            "r",
            encoding="utf-8"
        ) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            "styles.css not found"
        )

load_css()

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
<div style='text-align:center'>
<h1>🛡️ NetVision AI</h1>
<p>
Advanced Network Traffic Monitoring &
Threat Detection Platform
</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# DATABASE
# -----------------------------

def load_packets():

    try:

        conn = sqlite3.connect(
            "data/packets.db"
        )

        df = pd.read_sql_query(
            "SELECT * FROM packets",
            conn
        )

        conn.close()

        return df

    except Exception:

        return pd.DataFrame()

# -----------------------------
# LOAD DATA
# -----------------------------

df = load_packets()

# -----------------------------
# KPIs
# -----------------------------

total_packets = len(df)

anomalies = 0

active_connections = (
    df["src_ip"].nunique()
    if "src_ip" in df.columns
    else 0
)

health_score = max(
    100 - (anomalies * 2),
    0
)

display_kpis(
    total_packets,
    anomalies,
    active_connections,
    health_score
)

st.divider()

# -----------------------------
# MAIN DASHBOARD
# -----------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "🚨 Threat Center",
    "🌐 Network Analytics",
    "⚙️ SOC Dashboard"
])

# -----------------------------
# TAB 1
# -----------------------------

with tab1:

    st.subheader(
        "Network Overview"
    )

    if not df.empty:

        protocol_chart(df)

        packet_size_chart(df)

        generate_insights(df)

    else:

        st.info(
            "No packet data available."
        )

# -----------------------------
# TAB 2
# -----------------------------

with tab2:

    st.subheader(
        "Threat Monitoring"
    )

    if not df.empty:

        attack_timeline(df)

        threat_heatmap(df)

    else:

        st.info(
            "No threats detected."
        )

# -----------------------------
# TAB 3
# -----------------------------

with tab3:

    st.subheader(
        "Network Analytics"
    )

    if not df.empty:

        protocol_distribution(df)

        show_top_talkers(df)

    else:

        st.info(
            "No analytics data."
        )

# -----------------------------
# TAB 4
# -----------------------------

with tab4:

    soc_dashboard()

    network_health(
        anomalies=anomalies,
        threats=0
    )

# -----------------------------
# RAW DATA
# -----------------------------

st.divider()

with st.expander(
    "📁 View Packet Data"
):

    if not df.empty:

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning(
            "Database is empty."
        )

# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
"""
<div class='footer'>
NetVision AI © 2026
</div>
""",
unsafe_allow_html=True
)