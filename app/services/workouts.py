import pandas as pd
from io import BytesIO

def process_workouts(file_bytes: bytes):
    # Leer CSV desde memoria
    df = pd.read_csv(BytesIO(file_bytes), parse_dates=["date"])

    # Calcular métricas
    df["pace_min_per_km"] = df["duration_min"] / df["distance_km"]
    df["efficiency"] = df["distance_km"] / df["avg_hr"]

    # Resumen simple
    summary = {
        "total_sessions": int(len(df)),
        "total_distance_km": float(round(df["distance_km"].sum(), 2)),
        "total_duration_min": float(round(df["duration_min"].sum(), 1)),
        "avg_pace_min_per_km": float(round(df["pace_min_per_km"].mean(), 2)),
        "avg_hr": float(round(df["avg_hr"].mean(), 1)),
        "best_efficiency": float(round(df["efficiency"].max(), 3)),
    }

    return summary
