from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score

def train_model(df):

    df = df.copy()
    df["Overrun"] = (df["Actual_Cost"] > df["Estimated_Cost"]).astype(int)

    features = [
        "Length_km",
        "Voltage_kV",
        "Planned_Duration",
        "Contractor_Experience",
        "Material_Cost_Index",
        "Labor_Availability"
    ]

    X = df[features]
    y = df["Overrun"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        class_weight="balanced",
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)

    return model, features, acc, prec