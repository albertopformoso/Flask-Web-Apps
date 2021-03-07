from basic import db, Puppy


# CREATES ALL THE TABLES Model --> Db Table
db.create_all()

sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)


print(sam.id)  # None
print(frank.id)  # None

db.session.add_all([sam, frank])

# db.session.add(sam)
# db.session.add(frank)

db.session.commit()

print(sam.id)  # 1
print(frank.id)  # 2