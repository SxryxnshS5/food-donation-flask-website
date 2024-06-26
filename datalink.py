import os
from datetime import datetime

from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy import and_, or_
from sqlalchemy.exc import SQLAlchemyError

from app import db
from models import User, Advert, Message, Collection


def _connect():
    # connect to database, only use internally for testing
    load_dotenv()
    engine = sqlalchemy.create_engine(os.getenv('SQLALCHEMY_DATABASE_URI'))
    try:
        engine.connect()
        print("connected")
        return engine
    except SQLAlchemyError as e:
        print("error", e.__cause__)
        return None


def create_user(user):
    """Add a new user row to user table using a User object"""
    db.session.add(user)
    db.session.commit()


def create_advert(advert):
    """Add a new advert row to advert table using an Advert object"""
    db.session.add(advert)
    db.session.commit()


def create_order(order):
    """Add new order row to foodorder table"""
    db.session.add(order)
    db.session.commit()


def create_message(message):
    """Add a new message row to message table using an message object"""
    db.session.add(message)
    db.session.commit()


def get_available_ads():
    """returns list of adverts that are currently available to collect
        automatically marks out of date ads as unavailable
    """
    check_expiry()
    return Advert.query.filter_by(available=True).all()


def get_user(email):
    """returns a User object from the database using their username"""
    return User.query.filter_by(email=email).first()


def get_user_from_id(user_id):
    """returns a User object from the database using their username"""
    return User.query.filter_by(id=user_id).first()


def is_unique(email):
    """returns if a username isn't already in use"""
    return get_user(email) is None


def set_advert_unavailable(ad_id):
    """marks advert as unavailable using its ID"""
    ad = Advert.query.filter_by(adID=ad_id).first()
    ad.available = False
    db.session.commit()


def check_expiry():
    """finds and marks all adverts past their expiry date as unavailable"""
    # equivalent to UPDATE Advert SET available=False WHERE available AND expiry < now
    Advert.query.filter(
        and_(Advert.available, Advert.expiry < datetime.now())
    ).update({Advert.available: False})
    db.session.commit()


def update_details(database_user, updated_user):
    """updates old_user's details to have updated_user's attribtutes
        - note a new username must be unique
        - note role cannot be changed to admin here
    """
    if updated_user.role == "admin" and database_user.role != "admin":
        raise ValueError("Cannot change role to admin")
    if not is_unique(updated_user.email):
        raise ValueError("Username unavailable")

    database_user.email = updated_user.email
    database_user.password = updated_user.password
    database_user.first_name = updated_user.first_name
    database_user.surname = updated_user.surname
    database_user.dob = updated_user.dob
    database_user.address = updated_user.address
    database_user.role = updated_user.role
    db.session.commit()


def get_user_collections(collector_id):
    """return collections made by a user"""
    return Collection.query.filter_by(buyer=collector_id)


def get_conversations(user_id):
    """returns list of users who a user has had a conversation with"""
    q1 = User.query.join(Message, User.id == Message.receiver).filter_by(sender=user_id).distinct()
    q2 = User.query.join(Message, User.id == Message.sender).filter_by(receiver=user_id).distinct()
    return q1.union(q2).all()


def get_latest_message(user1_id, user2_id):
    """return message object most recently send between 2 users"""
    return Message.query.filter(
        or_(
            and_(Message.sender == user1_id, Message.receiver == user2_id),
            and_(Message.sender == user2_id, Message.receiver == user1_id),
        )
    ).order_by(Message.timestamp.desc()).first()

def get_message_history(user1_id, user2_id):
    """return all messages sent to between 2 users"""
    return Message.query.filter(
        or_(
            and_(Message.sender == user1_id, Message.receiver == user2_id),
            and_(Message.sender == user2_id, Message.receiver == user1_id),
        )
    ).order_by(Message.timestamp).all()


def delete_user(user):
    """removes user object's row in User table"""
    db.session.delete(user)
    db.session.commit()


def delete_advert(advert):
    """removes advert object's row in Advert table"""
    db.session.delete(advert)
    db.session.commit()


def delete_message(message):
    """removes message object's row in Message table"""
    db.session.delete(message)
    db.session.commit()


def delete_order(order):
    """removes order object's row in foodorder table"""
    db.session.delete(order)
    db.session.commit()
