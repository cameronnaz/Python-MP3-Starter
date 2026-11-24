""" users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]

def admin():
    for user in users:
        try:
            if user['role'] == "admin":
                print(user["name"])
        except KeyError:
            continue
admin() """

#before try and except, it wouldnt work because of a key error. If you except it it runs the code without the error


def mp3():
    pygame.mixer.music.load()