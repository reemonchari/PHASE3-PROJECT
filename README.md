```
# Fitness Fusion - Virtual Fitness Coach (CLI App)

## 📌 Introduction
Welcome to **Fitness Fusion**, a CLI-based virtual fitness coach that helps users:
- Set fitness goals (e.g., weight loss, muscle gain)
- Log workouts easily
- Track progress with a progress tracking system
- Generate reports summarizing fitness activities
- Receive motivational quotes and fitness tips

This project is built using **Python, SQLAlchemy ORM, and Click for CLI handling**.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/reemonchari/PHASE3-PROJECT.git
cd PHASE3-PROJECT
```

### 2️⃣ Set Up a Virtual Environment
```
pipenv install
pipenv shell
```

### 3️⃣ Initialize and Migrate the Database
```
cd lib/db
alembic upgrade head
```

### 4️⃣ Seed the Database (Optional)
```
python seed.py
```

---

## 🎮 Usage
Run the CLI application using:
```
python cli.py --help
```

### Available Commands
```
python cli.py add-user           # Add a new user
python cli.py list-users         # List all users
python cli.py delete-user        # Delete a user
python cli.py add-workout        # Add a workout for a user
python cli.py view-workouts      # View all workouts for a user
```

---

## 🗄️ Database Schema
### Tables:
1. **User** (*id, name, fitness_goal*)
2. **Workout** (*id, user_id, workout_type, duration*)
   - One-to-Many relationship: **User → Workouts**

---

## 🏆 Features
✅ User Management (Create, List, Delete Users)  
✅ Workout Logging (Add & View Workouts)  
✅ Progress Tracking  
✅ Motivational Tips  
✅ Data Validation & Error Handling  
✅ Alembic Migrations for DB Schema  
✅ Faker for Seeding Data  

---

## 🛠 Tech Stack
- **Python** (Main Language)
- **SQLAlchemy ORM** (Database Management)
- **Click** (For CLI Interactions)
- **Alembic** (Migrations)
- **Faker** (Mock Data)

---

## ❗ Important Notes
- Ensure you are running commands **inside the Pipenv shell** (`pipenv shell`).
- Always run `alembic upgrade head` after modifying database models.
- If you encounter errors, check dependencies using `pipenv graph`.

---

## 👨‍💻 Author
**Monchari Ree**  
GitHub: [reemonchari](https://github.com/reemonchari)

---

## 📜 License
This project is licensed under the **MIT License**.
```

