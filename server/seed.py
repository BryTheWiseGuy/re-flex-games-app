from random import randint, choice as rc

from faker import Faker

from app import app
from models import db, User, Game

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
