from fastapi import APIRouter, UploadFile, File
from app.services.workouts import process_workouts
from app.services.db import Workout, SessionLocal, create_db_and_tables
import pandas as pd

router = APIRouter()


# Inicializar la base de datos si es necesario
create_db_and_tables()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Forzar la creación de la base de datos y tablas antes de operar
    create_db_and_tables()
    content = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(content), parse_dates=["date"])
    session = SessionLocal()
    nuevos = 0
    for _, row in df.iterrows():
        exists = session.query(Workout).filter_by(csv_id=int(row["id"])).first()
        if not exists:
            workout = Workout(
                csv_id=int(row["id"]),
                date=row["date"].date() if hasattr(row["date"], 'date') else row["date"],
                duration_min=float(row["duration_min"]),
                distance_km=float(row["distance_km"]),
                avg_hr=int(row["avg_hr"]),
                max_hr=int(row["max_hr"]),
                calories=int(row["calories"])
            )
            session.add(workout)
            nuevos += 1
    session.commit()
    session.close()
    return {"msg": f"Carga completada. Entrenamientos nuevos agregados: {nuevos}"}


# Endpoint para obtener un workout individual por id desde la base de datos
@router.get("/workouts/{workout_id}")
async def get_workout(workout_id: int):
    session = SessionLocal()
    workout = session.query(Workout).filter_by(id=workout_id).first()
    session.close()
    if not workout:
        return {"error": "Workout no encontrado"}
    return {
        "id": workout.id,
        "csv_id": workout.csv_id,
        "date": str(workout.date),
        "duration_min": workout.duration_min,
        "distance_km": workout.distance_km,
        "avg_hr": workout.avg_hr,
        "max_hr": workout.max_hr,
        "calories": workout.calories
    }


# Endpoint para obtener todos los workouts desde la base de datos
@router.get("/workouts/")
async def get_workouts():
    session = SessionLocal()
    workouts = session.query(Workout).all()
    session.close()
    return [
        {
            "id": w.id,
            "csv_id": w.csv_id,
            "date": str(w.date),
            "duration_min": w.duration_min,
            "distance_km": w.distance_km,
            "avg_hr": w.avg_hr,
            "max_hr": w.max_hr,
            "calories": w.calories
        }
        for w in workouts
    ]
    
# Endpoint para eliminar un workout por id
@router.delete("/workouts/{workout_id}")
async def delete_workout(workout_id: int):
    session = SessionLocal()
    workout = session.query(Workout).filter_by(id=workout_id).first()
    if not workout:
        session.close()
        return {"error": "Workout no encontrado"}
    session.delete(workout)
    session.commit()
    session.close()
    return {"msg": f"Workout con id {workout_id} eliminado correctamente"}
