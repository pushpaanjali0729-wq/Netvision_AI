# dashboard/geo_threat_map.py

import streamlit as st
import pandas as pd
import pydeck as pdk


def geo_threat_map():

    data = pd.DataFrame({

        "lat": [17.6868, 28.6139],

        "lon": [83.2185, 77.2090]
    })

    layer = pdk.Layer(

        "ScatterplotLayer",

        data,

        get_position="[lon, lat]",

        get_radius=10000
    )

    view = pdk.ViewState(

        latitude=20,

        longitude=80,

        zoom=4
    )

    st.pydeck_chart(

        pdk.Deck(

            layers=[layer],

            initial_view_state=view
        )
    )