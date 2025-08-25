
# Sports Tracker API

REST API to process and analyze sports workouts using FastAPI and SQLite.

## Project Structure

- `app/main.py`: FastAPI application entry point.
- `app/api/routes.py`: API endpoints.
- `app/services/workouts.py`: Workout processing logic.
- `app/services/db.py`: Database models and connection.
- `data/`: Folder for CSV and SQLite database.
- `tests/`: Unit tests.

## How to Run the Project

1. Install dependencies:
	 ```bash
	 pip install -r requirements.txt
	 ```

2. Start the FastAPI server:
	 ```bash
	 uvicorn app.main:app --reload
	 ```

3. The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

4. Interactive documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Available Endpoints

### Upload Workouts from CSV
**POST** `/upload/`
- Upload a CSV file with workouts. The file must have columns: `id`, `date`, `duration_min`, `distance_km`, `avg_hr`, `max_hr`, `calories`.
- Example (using curl):
	```bash
	curl -X POST -F "file=@data/workouts.csv" http://127.0.0.1:8000/upload/
	```

### Upload Workout from JSON
**POST** `/uploadJson`
- Add a single workout by sending a JSON object.
- `csv_id` is optional. If provided, it must be unique. If omitted or null, it will be ignored.
- Example:
	```json
	{
		"date": "2025-08-15",
		"duration_min": 40,
		"distance_km": 7.5,
		"avg_hr": 135,
		"max_hr": 165,
		"calories": 500
	}
	```

### Get All Workouts
**GET** `/workouts/`
- Returns a list of all workouts in the database.

### Get Workout by ID
**GET** `/workouts/{workout_id}`
- Returns a single workout by its database ID.

### Delete Workout by ID
**DELETE** `/workouts/{workout_id}`
- Deletes a workout by its database ID.

## Running Tests

```bash
pytest
```
