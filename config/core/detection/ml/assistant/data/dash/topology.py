# dashboard/topology.py

import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st


def draw_topology(df):

    graph = nx.Graph()

    for _, row in df.iterrows():

        graph.add_edge(

            row["src_ip"],

            row["dst_ip"]
        )

    fig = plt.figure(
        figsize=(10, 6)
    )

    nx.draw_networkx(
        graph,
        with_labels=True
    )

    st.pyplot(fig)