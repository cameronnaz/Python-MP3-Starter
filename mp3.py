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

#before try and except, it wouldnt work because of a key error. If
# . you except it it runs the code without the error


def mp3():
    import pygame
    pygame.init()

    pygame.display.set_mode((400, 500))


    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.mixer.music.load()
#delete here if necesarry 
# Python program to change 
# the Pygame icon

# Import the library Pygame
import pygame

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
screen = pygame.display.set_mode([600, 400])

# Take image as input
img = pygame.image.load('9 cover.jpg')

# Set image as icon
pygame.display.set_icon(img)


running = True


while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 0))

    
    pygame.draw.circle(screen, (0, 0, 0), (300, 200), 75)

    
    pygame.display.update()

pygame.quit()


mp3()