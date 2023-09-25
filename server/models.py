from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import validates

from config import db, bcrypt

# Models go here!
