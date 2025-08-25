
import pandas as pd
from io import BytesIO


def get_all_workouts():
    df = pd.read_csv('data/workouts.csv', parse_dates=["date"])
    workouts = df.to_dict(orient="records")
    return workouts


def get_workout_by_id(workout_id: int):
    df = pd.read_csv('data/workouts.csv', parse_dates=["date"])
    workout = df[df['id'] == workout_id]
    if workout.empty:
        return None
    return workout.to_dict(orient="records")[0]

