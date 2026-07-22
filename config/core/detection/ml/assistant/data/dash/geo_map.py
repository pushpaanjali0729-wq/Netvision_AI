# dashboard/geo_map.py

import streamlit as st
import pydeck as pdk
import pandas as pd


def show_map():

    data = pd.DataFrame({

        "lat": [17.6868],

        "lon": [83.2185]
    })

    st.pydeck_chart(

        pdk.Deck(

            initial_view_state=
            pdk.ViewState(

                latitude=17.6868,

                longitude=83.2185,

                zoom=8
            ),

            layers=[

                pdk.Layer(

                    "ScatterplotLayer",

                    data,

                    get_position=
                    "[lon, lat]",

                    get_radius=5000
                )
            ]
        )
    )