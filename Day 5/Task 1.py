def create_user(name, age, role):
    user = {
        "name": name.title(), 
        "age": age,
        "role": role
    }
    return user
users = []

users.append(create_user("Nivetha", 25, "developer"))
users.append(create_user("Dilli", 22, "Business man"))

for user in users:
    print(user)