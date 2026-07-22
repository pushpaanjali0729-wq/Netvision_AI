# ml/forecasting.py

import pandas as pd


class TrafficForecaster:

    def forecast(
            self,
            df
    ):

        avg_packets = len(df)

        prediction = avg_packets * 1.1

        return {

            "current": avg_packets,

            "predicted": int(prediction)
        }