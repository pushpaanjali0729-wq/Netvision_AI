import pandas as pd


def create_features(df):

    df["packet_length_log"] = (
        df["packet_length"] + 1
    )

    df["packet_length_log"] = (
        df["packet_length_log"]
        .apply(lambda x: x ** 0.5)
    )

    return df