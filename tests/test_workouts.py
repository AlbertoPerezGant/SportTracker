import pytest
from app.services.workouts import process_workouts

# Puedes agregar más tests según crezca la lógica

def test_process_workouts():
    csv_bytes = b"date,duration_min,distance_km,avg_hr,max_hr,calories\n2025-08-01,45,8.5,145,175,560\n2025-08-03,30,5.2,152,180,350\n2025-08-05,60,10.0,138,170,640\n"
    result = process_workouts(csv_bytes)
    assert result["total_sessions"] == 3
    assert result["total_distance_km"] == 23.7
