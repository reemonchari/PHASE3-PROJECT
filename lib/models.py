from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# Initialize the Base class
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    fitness_goal = Column(String, nullable=False)

    workouts = relationship("Workout", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(name={self.name}, goal={self.fitness_goal})>"

# Define Workout model
class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    workout_type = Column(String, nullable=False)
    duration = Column(Integer)  
    date = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="workouts")

    def __repr__(self):
        return f"<Workout(type={self.workout_type}, duration={self.duration} mins)>"

# Database connection setup
DATABASE_URL = "sqlite:///fitness_fusion.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
