# from model import SessionLocal, User


from model import Person, User
from session import SessionLocal


session = SessionLocal()

# user = User(name="Lody", age=90)
# user1 = User(name="Lui", age=34)
# user2 = User(name="Paul", age=67)
# user3 = User(name="Toti", age=23)
# # session.add(user)

# session.add_all([user1,user2,user3])
# session.commit()

# users = session.query(User).all()
# users = session.query(User).filter_by(id=1).one_or_none()

# print(users.name)
# # users.name="Linagrd"
# session.delete(users)
# session.commit()
# user = users[0]
# print(user)
# print(user.name)
# print(user.age)

# names = ["Doe", "Paul", "Ana", "JK"]
# ages = [20, 22, 28, 21]
# for x in range(20):
#     user = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)
# session.commit()

# users = session.query(User).order_by(User.age, User.name).all()
# for user in users:
#     print(f"User ID {user.id}, User age:{user.age} User name:{user.name}")

users = session.query(User).all()
# for user in users:
#     print(f"User ID {user.id}, User age:{user.age} User name:{user.name}")
# user_filtered = session.query(User).filter(User.age < 25, User.name == "Ana").all()
# for user in user_filtered:
#     print(f"User ID {user.id}, User age:{user.age} User name:{user.name}")

# print(f"User length:{len(user_filtered)}")

# user1 = session.query(User).filter_by(age=20).all()
# for user in user1:
#     print(f"User ID {user.id}, User age:{user.age} User name:{user.name}")

# user2 = session.query(User).where(or_(User.age <= 20, User.name == "Paul")).all()
# user2 = session.query(User).where(and_(User.age <= 20, User.name == "Paul")).all()
# user2 = session.query(User).where((User.age <= 20) & (User.name == "Paul")).all()
# user2 = session.query(User).where((User.age <= 20) | (User.name == "Paul")).all()
# # user2 = session.query(User).where(not_(User.age == 20)).all()
# user2 = (
#     session.query(User)
#     .where(or_(not_(User.name == "Paul"), and_(User.age == 21, User.age == 22)))
#     .all()
# )
# user2 = session.query(User).group_by(User.name).all()
# user2 = session.query(User.age, func.count(User.id)).group_by(User.age).all()
# user_tuple = (
#     session.query(User.age, func.count(User.id))
#     .filter(User.age > 23)
#     .order_by(User.age)
#     .filter(User.age < 30)
#     .group_by(User.age)
#     .all()
# )
# for age, count in user_tuple:

#     print(f"Age:{age} - {count} users")
# print(user2)
# for user in user2:
#     print(f"User ID {user.id}, User age:{user.age} User name:{user.name}")


# user1 = User(name="Lody", age=90)
# user2 = User(name="Lui", age=67)

# address1 = Address(name="Dodoma", state="Tanzania", zip_code=234)
# address2 = Address(name="Dar", state="Tanzania", zip_code=123)
# address3 = Address(name="Arusha", state="Tanzania", zip_code=678)

# user1.addresses.extend([address1, address2])
# user2.addresses.append(address3)

# session.add(user1)
# session.add(user2)
# session.commit()

# print(f"{user1.addresses = }")
# print(f"{user2.addresses = }")
# print(f"{address1.user = }")

person1 = Person(username="Lody")
person2 = Person(username="Lui")
person3 = Person(username="Pogba")

person1.following.append(person2)
person2.following.append(person3)
person3.following.append(person1)

session.add_all([person1, person2, person3])
session.commit()

print(f"{person1.following = }")
print(f"{person2.following = }")
print(f"{person3.following = }")
