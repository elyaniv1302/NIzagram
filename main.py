from classes.Post import Post
from helpers import mouse_in_button,read_comment_from_user,screen
from buttons import like_button
from test_methods import test_comment
import pygame
from buttons import comment_button ,click_post_button
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.Comment import Comment

def main():

    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here     # אנחנו נותנים שם של משנתה ואז עושים שווה רושמים את השם של המחלקה שאנחנו רוצים שהאובייקט יהיה מהסוג שלה ואז רושמים בתוך סוגריים עגולות את המשתנים שצריך בבנאי
    post1 = Post("Images/noa_kirel.jpg","netivot","noa kirel")
    post2 = Post("Images/ronaldo.jpg","beer seva", "i love elyaniv ")
    post_list = [post1, post2]
    current_index = 0
    current_post = post_list[current_index]








    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get(): # עבור כל אירוע
            if event.type == pygame.QUIT:

                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                place = event.pos  #המיקום של הלחיצה על העכבר
                if mouse_in_button(like_button,place):
                    current_post.add_like()

                if mouse_in_button(comment_button,place):
                  comment1 = read_comment_from_user()
                  current_post.add_comment(comment1)

                if mouse_in_button(click_post_button, place):
                    if (current_index >= len(post_list)-1):
                        current_index = 0
                    else:
                        current_index += 1
                    current_post = post_list[current_index]























                  # Display the background, presented Image, likes, comments, tags and
        # location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        current_post.display()


        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        # If we want faster game - increase the parameter.
        clock.tick(60)

    pygame.quit()
    quit()


main()
