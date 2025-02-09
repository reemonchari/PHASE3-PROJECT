# 🏋️‍♂️ Fitness Fusion CLI

**Fitness Fusion** is a **command-line application** designed to help users set fitness goals, log workouts, track progress, and stay motivated on their fitness journey.

## 📌 Features

- **Set Fitness Goals** (e.g., weight loss, muscle gain)
- **Log Workouts** with ease
- **Track Progress** and view workout history
- **Generate Reports** summarizing fitness activities
- **Receive Motivational Quotes & Fitness Tips**

## 🛠️ Technologies Used

- **Python** (CLI functionality)
- **SQLAlchemy** (Database ORM)
- **SQLite** (Database storage)
- **Click or Fire** (Command-line handling)
- **Alembic** (Database migrations)

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/fitness-fusion-cli.git
   cd fitness-fusion-cli
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```sh
   alembic upgrade head
   python seed.py  # Populate the database with sample data
   ```

## 📌 Usage

Run the CLI using:
```sh
python cli.py --help
```

### Available Commands

- **List all users:**
  ```sh
  python cli.py list-users
  ```

- **View a user's workouts:**
  ```sh
  python cli.py view-workouts --user_id <user_id>
  ```

- **Add a workout:**
  ```sh
  python cli.py add-workout --user_id <user_id> --name "Cardio" --duration 30
  ```

- **Update a user's fitness goal:**
  ```sh
  python cli.py update-goal --user_id <user_id> --goal "Muscle Gain"
  ```

- **Delete a workout:**
  ```sh
  python cli.py delete-workout --workout_id <workout_id>
  ```

## 📜 License

This project is open-source and available under the **MIT License**.
