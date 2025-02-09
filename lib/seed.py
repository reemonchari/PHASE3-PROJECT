import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from models import session, User, Workout
from faker import Faker

fake = Faker()

user1 = User(name=fake.name(), fitness_goal="Muscle Gain")
user2 = User(name=fake.name(), fitness_goal="Weight Loss")

session.add_all([user1, user2])
session.commit()


workouts = [
    Workout(user_id=user1.id, workout_type="Strength Training", duration=45),
    Workout(user_id=user1.id, workout_type="Cardio", duration=30),
    Workout(user_id=user2.id, workout_type="Yoga", duration=60)
]

session.add_all(workouts)
session.commit()

print("Database seeded successfully! 🎉")
