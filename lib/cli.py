import click
from models import session, User, Workout

@click.group()
def cli():
    """Fitness Fusion - CLI Virtual Fitness Coach"""
    pass

@cli.command()
@click.option('--name', prompt="Enter your name", help="User's name")
@click.option('--goal', prompt="Enter your fitness goal", help="Fitness goal (e.g., Weight Loss, Muscle Gain)")
def add_user(name, goal):
    """Add a new user"""
    user = User(name=name, fitness_goal=goal)
    session.add(user)
    session.commit()
    click.echo(f"User {name} added successfully! ✅")

@cli.command()
@click.option('--user_id', prompt="Enter user ID", type=int)
@click.option('--type', prompt="Workout Type", help="Type of workout (e.g., Cardio, Strength Training)")
@click.option('--duration', prompt="Duration (in minutes)", type=int)
def add_workout(user_id, type, duration):
    """Log a workout for a user"""
    user = session.qet(User, user_id)
    if user:
        workout = Workout(user_id=user_id, workout_type=type, duration=duration)
        session.add(workout)
        session.commit()
        click.echo(f"Workout '{type}' logged for {user.name}! 🏋️‍♂️")
    else:
        click.echo("User not found! ❌")

@cli.command()
@click.option('--user_id', prompt="Enter user ID", type=int)
def view_workouts(user_id):
    """View all workouts for a user"""
    user = session.get(User, user_id)
    if user:
        click.echo(f"Workout History for {user.name}:")
        for w in user.workouts:
            click.echo(f"- {w.workout_type} ({w.duration} mins)")
    else:
        click.echo("User not found! ❌")

@cli.command()
def list_users():
    """List all users"""
    users = session.get(User).all()
    if users:
        for user in users:
            click.echo(f"ID: {user.id} | {user.name} | Goal: {user.fitness_goal}")
    else:
        click.echo("No users found.")

@cli.command()
@click.option('--user_id', prompt="Enter user ID", type=int)
def delete_user(user_id):
    """Delete a user"""
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        click.echo(f"User {user.name} deleted! ❌")
    else:
        click.echo("User not found!")

if __name__ == '__main__':
    cli()
