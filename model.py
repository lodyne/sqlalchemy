from sqlalchemy import Column, ForeignKey, Integer, String

# from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, Mapped, mapped_column

# from sqlalchemy.ext.declarative import declarative_base

# SQLITE_URL = "sqlite:///./user.db"

from session import Base, engine

# engine = create_engine(SQLITE_URL, connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# Base = declarative_base()


# class Address(Base):
#     __tablename__ = "addresses"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     state = Column(String)
#     zip_code = Column(Integer)
#     user_id = Column(ForeignKey("users.id"))
#     user = relationship("User", back_populates="addresses")

#     def __repr__(self):
#         return f"User ID {self.id}, username {self.name}, state {self.state}"


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)
#     addresses = relationship("Address")

#     def __repr__(self):
#         return f"User ID {self.id}, username {self.name}"


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"User ID {self.id}, username {self.name}, state {self.state}"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship()

    def __repr__(self):
        return f"User ID {self.id}, username {self.name}"


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"

    person_id = Column(Integer, ForeignKey("persons.id"))
    following_id = Column(Integer, ForeignKey("persons.id"))


class Person(BaseModel):
    __tablename__ = "persons"

    username = Column(String)
    # following_id = Column(Integer, ForeignKey("persons.id"))
    # following = relationship("Person", remote_side=[id], uselist=True)
    following = relationship(
        "Person",
        secondary="following_association",
        primaryjoin=("FollowingAssociation.person_id==Person.id"),
        secondaryjoin=("FollowingAssociation.following_id==Person.id"),
    )

    def __repr__(self):
        return (
            f"Person ID {self.id}, username {self.username}, following {self.following}"
        )


Base.metadata.create_all(engine)
