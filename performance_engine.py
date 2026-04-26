def calculate_variance(df):

    if df.empty:
        return df

    df = df.copy()

    df["Cost_Variance"] = df["Actual_Cost"] - df["Estimated_Cost"]
    df["Schedule_Variance"] = df["Actual_Duration"] - df["Planned_Duration"]

    return df
