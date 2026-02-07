from auth.login import login_user

user, msg = login_user(
    "kartavya@gmail.com",
    "pass123"
)

print(msg)
print(user)
