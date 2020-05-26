"""
File: my_pet_hedgehog.py
----------------
This program generates an interactive virtual pet hedgehog. There are five
activities to partake in, a status bar that reflects the hedgehog's "mood"
based on four different criteria and a feedback bar that displays the
hedgehog's "feelings".
"""

import time
import tkinter as tk
from PIL import ImageTk, Image

# Setting image constants for the animation.
HEDGEHOG_IMG = 'images/noun_Hedgehog.jpg'
HEDGEHOG_BATHE_IMG = 'images/bathing_Hedgehog_3.jpg'
HEDGEHOG_BATHE_IMG_2 = 'images/bathing_Hedgehog_4.jpg'
HEDGEHOG_FEED_IMG = 'images/feed_Hedgehog.jpg'
HEDGEHOG_FEED_IMG_2 = 'images/feed_Hedgehog_bite.jpg'
HEDGEHOG_LOVE_IMG = 'images/love_Hedgehog_1.jpg'
HEDGEHOG_LOVE_IMG_2 = 'images/love_Hedgehog_2.jpg'
HEDGEHOG_LOVE_IMG_3 = 'images/love_Hedgehog_3.jpg'
HEDGEHOG_PLAY_IMG = 'images/basketball_Hedgehog_1.jpg'
HEDGEHOG_PLAY_IMG_2 = 'images/basketball_Hedgehog_3.jpg'
HEDGEHOG_SLEEP_IMG = 'images/teepee_Hedgehog_1.jpg'
HEDGEHOG_SLEEP_IMG_2 = 'images/teepee_Hedgehog_2.jpg'
HEDGEHOG_SLEEP_IMG_3 = 'images/teepee_Hedgehog_3.jpg'

ANIMATION_FPS = 0.25

# Setting limits on each mood in order to encourage engagement with
# various activities.
MOOD_MINIMUM = 0
MOOD_MAXIMUM = 15

# Dictionary of criteria used to judge a given mood. The goal is to maintain
# a balance between each criteria: cleanliness indicates how clean the hedgehog
# is, the goal is to keep this value higher than zero, the higher the value,
# the cleaner the hedgehog; energy indicates the amount of energy the hedgehog
# has, the goal is to keep this value higher than zero; happiness indicates how
# happy the hedgehog is, the goal is to keep this value higher than zero; hunger
# indicates how hungry the hedgehog is, the goal is to keep this value closer to
# zero, the lower the value, the more satisfied the hedgehog.
hedgehog_info = {'Cleanliness': 10,
                 'Energy': 10,
                 'Happiness': 10,
                 'Hunger': 10}

# Creates tkinter window.
window = tk.Tk()
window.title('My Pet Hedgehog')
window.geometry('{}x{}'.format(650, 350))

# Creates all of the main frames.
top_frame = tk.Frame(window, width=450, height=50, pady=3, bg="orange")
center = tk.Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
btm_frame = tk.Frame(window, width=450, height=45, pady=3, bg="orange")

# Layouts all the main frames.
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")

# Creates the center widgets.
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = tk.Frame(center, width=100, height=190)
ctr_mid = tk.Frame(center, width=250, height=190, padx=3, pady=3)
ctr_right = tk.Frame(center, width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

# Enables the ability to update the status and feedback bar in window, after
# every activity.
info_string = tk.StringVar()
hedgehog_sayings = tk.StringVar()


def get_initial_hedgehog():
    """
    This function initializes the pet hedgehog image and is used as a reset
    image after every animation.
    """
    pet_image = Image.open(HEDGEHOG_IMG)
    pet_image = pet_image.resize((504 // 2, 474 // 2), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(pet_image)

    return img


def reset_hedgehog():
    """
    This function resets the hedgehog image after every animation.
    """
    img = get_initial_hedgehog()
    panel.configure(image=img)
    panel.image = img
    panel.update()


img = get_initial_hedgehog()
panel = tk.Label(ctr_mid, image=img)


def handle_bathe():
    """
    Every "activity" or button selected has a positive and/or negative effect on the
    criteria that influences the hedgehog's mood. Bathing increases the hedgehog's
    cleanliness, but decreases happiness. Once selected, the button will either prompt
    the user with a phrase reflecting the hedgehog's current feeling and an animation,
    or a phrase noting the cleanliness criteria has reached its maximum limit.
    """
    disable_buttons()

    if hedgehog_info['Cleanliness'] < MOOD_MAXIMUM:
        update_hedgehog_sayings('I hate bathing')
        hedgehog_info['Happiness'] -= 1
        hedgehog_info['Cleanliness'] += 3
        bathe_animation()
    else:
        update_hedgehog_sayings('I am as clean as can be!')
        hedgehog_info['Cleanliness'] += 1

    update_stats()


def bathe_animation():
    """
    This function executes the hedgehog bathing.
    """
    bathe_img = open_animation_image(HEDGEHOG_BATHE_IMG)
    bathe_img_2 = open_animation_image(HEDGEHOG_BATHE_IMG_2)

    for i in range(4):
        update_panel(bathe_img)
        update_panel(bathe_img_2)

    reset_hedgehog()


def handle_feed():
    """
    Every "activity" or button selected has a positive and/or negative effect on the
    criteria that influences the hedgehog's mood. Feeding increases the hedgehog's
    energy, and decreases hunger. Once selected, the button will either prompt the
    user with a phrase reflecting the hedgehog's current feeling and an animation,
    or a phrase noting the hunger criteria has reached its maximum limit.
    """
    if not check_cleanliness():
        return

    disable_buttons()

    if MOOD_MINIMUM < hedgehog_info['Hunger'] <= MOOD_MAXIMUM:
        update_hedgehog_sayings('That was yummy')
        hedgehog_info['Energy'] += 1
        hedgehog_info['Hunger'] -= 2
        feed_animation()
    else:
        update_hedgehog_sayings('I am too full to eat')
        hedgehog_info['Cleanliness'] += 1

    update_stats()


def feed_animation():
    """
    This function executes the hedgehog eating.
    """
    feed_img = open_animation_image(HEDGEHOG_FEED_IMG)
    feed_img_2 = open_animation_image(HEDGEHOG_FEED_IMG_2)

    for i in range(4):
        update_panel(feed_img)
        update_panel(feed_img_2)

    reset_hedgehog()


def handle_love():
    """
    Every "activity" or button selected has a positive and/or negative effect on the
    criteria that influences the hedgehog's mood. Loving increases the hedgehog's
    happiness. Once selected, the button will either prompt the user with a phrase
    reflecting the hedgehog's current feeling and an animation, or a phrase
    noting the love criteria has reached its maximum limit.
    """
    if not check_cleanliness():
        return

    disable_buttons()

    if MOOD_MINIMUM < hedgehog_info['Happiness'] < MOOD_MAXIMUM:
        update_hedgehog_sayings('I love you')
        hedgehog_info['Happiness'] += 1
        love_animation()
    else:
        update_hedgehog_sayings('Thanks, but I need some space')
        hedgehog_info['Cleanliness'] += 1

    update_stats()


def love_animation():
    """
    This function executes loving the hedgehog.
    """
    love_img = open_animation_image(HEDGEHOG_LOVE_IMG)
    love_img_2 = open_animation_image(HEDGEHOG_LOVE_IMG_2)
    love_img_3 = open_animation_image(HEDGEHOG_LOVE_IMG_3)

    for i in range(2):
        update_panel(love_img)
        update_panel(love_img_2)
        update_panel(love_img_3)
        reset_hedgehog()
        time.sleep(ANIMATION_FPS)


def handle_play():
    """
    Every "activity" or button selected has a positive and/or negative effect on the
    criteria that influences the hedgehog's mood. Playing increases the hedgehog's
    happiness and hunger, but decreases energy. Once selected, the button will either
    prompt the user with a phrase reflecting the hedgehog's current feeling and an
    animation, or a phrase noting either the energy criteria has reached its minimum
    limit or the hunger criteria has reached its maximum limit.
    """

    if not check_cleanliness():
        return

    disable_buttons()

    if hedgehog_info['Energy'] <= MOOD_MINIMUM:
        update_hedgehog_sayings('Sorry I have no energy, I need sleep!')
        hedgehog_info['Cleanliness'] += 1
    elif hedgehog_info['Hunger'] >= MOOD_MAXIMUM:
        update_hedgehog_sayings('I am too hungry to play!')
        hedgehog_info['Cleanliness'] += 1
    else:
        update_hedgehog_sayings('Haha that was fun')
        hedgehog_info['Energy'] -= 2
        hedgehog_info['Happiness'] += 1
        hedgehog_info['Hunger'] += 1
        play_animation()

    update_stats()


def play_animation():
    """
    This function executes the hedgehog playing.
    """
    play_img = open_animation_image(HEDGEHOG_PLAY_IMG)
    play_img_2 = open_animation_image(HEDGEHOG_PLAY_IMG_2)

    for i in range(4):
        update_panel(play_img)
        update_panel(play_img_2)

    reset_hedgehog()


def handle_sleep():
    """
    Every "activity" or button selected has a positive and/or negative effect on the
    criteria that influences the hedgehog's mood. Sleeping increases the hedgehog's
    energy. Once selected, the button will either prompt the user with a phrase reflecting
    the hedgehog's current feeling and an animation, or a phrase noting the energy criteria
    has reached its maximum limit.
    """
    if not check_cleanliness():
        return

    disable_buttons()

    if hedgehog_info['Energy'] < MOOD_MAXIMUM:
        update_hedgehog_sayings('Hmm... bedtime')
        hedgehog_info['Energy'] += 3
        sleep_animation()
    else:
        update_hedgehog_sayings('I feel very rested and do not want to sleep')
        hedgehog_info['Cleanliness'] += 1

    update_stats()


def sleep_animation():
    """
    This function executes the hedgehog sleeping.
    """
    sleep_img = open_animation_image(HEDGEHOG_SLEEP_IMG)
    sleep_img_2 = open_animation_image(HEDGEHOG_SLEEP_IMG_2)
    sleep_img_3 = open_animation_image(HEDGEHOG_SLEEP_IMG_3)

    for i in range(4):
        update_panel(sleep_img)
        update_panel(sleep_img_2)
        update_panel(sleep_img_3)

    reset_hedgehog()


def open_animation_image(image_path):
    """
    This function opens the images used in the animation for each button.
    """
    pet_image = Image.open(image_path)
    width, height = pet_image.size
    pet_image = pet_image.resize((width // 2, height // 2), Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pet_image)

    return tk_image


def update_panel(image):
    """
    This function updates the images used in the animation for each button.
    """
    panel.configure(image=image)
    panel.image = image
    panel.update()
    time.sleep(ANIMATION_FPS)


# Layouts the bathe button.
bathe_button = tk.Button(ctr_left,
                         text="Bathe \n🧼",
                         font=("Helvetica", 16),
                         width=10,
                         height=3,
                         fg="orange",
                         command=handle_bathe)
bathe_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Layouts the feed button.
feed_button = tk.Button(ctr_left,
                        text="Feed \n🐛",
                        font=("Helvetica", 16),
                        width=10,
                        height=3,
                        fg="orange",
                        command=handle_feed)
feed_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Layouts the love button.
love_button = tk.Button(ctr_left,
                        text="Love \n❤️❤️️️",
                        font=("Helvetica", 16),
                        width=10,
                        height=3,
                        fg="orange",
                        command=handle_love)
love_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Layouts the play button.
play_button = tk.Button(ctr_right,
                        text="Play \n🏀",
                        font=("Helvetica", 16),
                        width=10,
                        height=3,
                        fg="orange",
                        command=handle_play)
play_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Layouts the sleep button.
sleep_button = tk.Button(ctr_right,
                         text="Sleep \n💤",
                         font=("Helvetica", 16),
                         width=10,
                         height=3,
                         fg="orange",
                         command=handle_sleep)
sleep_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def disable_buttons():
    """
    Disables all buttons once a button has been selected in order to prevent
    a build up of commands while the animation is played.
    """
    bathe_button.config(state=tk.DISABLED)
    feed_button.config(state=tk.DISABLED)
    love_button.config(state=tk.DISABLED)
    play_button.config(state=tk.DISABLED)
    sleep_button.config(state=tk.DISABLED)


def enable_buttons():
    """
    Enables buttons after the "mood" criteria have been updated.
    """
    bathe_button.config(state=tk.NORMAL)
    feed_button.config(state=tk.NORMAL)
    love_button.config(state=tk.NORMAL)
    play_button.config(state=tk.NORMAL)
    sleep_button.config(state=tk.NORMAL)


def check_cleanliness():
    """
    Every "activity" or button selected reduces the hedgehog's cleanliness,
    in order to incentivize the user to bathe the hedgehog.
    """
    if hedgehog_info['Cleanliness'] <= MOOD_MINIMUM:
        update_hedgehog_sayings('I am too dirty to do anything!')
        return False
    else:
        hedgehog_info['Cleanliness'] -= 1
        return True


def update_stats():
    """
    This function updates the criteria used to reflect the hedgehog's mood:
    cleanliness, energy, happiness and hunger. The criteria are updated after
    every activity.
    """

    # Ensure all criteria are within limits, if not the limits are set to
    # its respective minimum and maximum.
    if hedgehog_info['Cleanliness'] > MOOD_MAXIMUM:
        hedgehog_info['Cleanliness'] = MOOD_MAXIMUM

    if hedgehog_info['Cleanliness'] < MOOD_MINIMUM:
        hedgehog_info['Cleanliness'] = MOOD_MINIMUM

    if hedgehog_info['Energy'] > MOOD_MAXIMUM:
        hedgehog_info['Energy'] = MOOD_MAXIMUM

    if hedgehog_info['Energy'] < MOOD_MINIMUM:
        hedgehog_info['Energy'] = MOOD_MINIMUM

    if hedgehog_info['Happiness'] > MOOD_MAXIMUM:
        hedgehog_info['Happiness'] = MOOD_MAXIMUM

    if hedgehog_info['Happiness'] < MOOD_MINIMUM:
        hedgehog_info['Happiness'] = MOOD_MINIMUM

    if hedgehog_info['Hunger'] > MOOD_MAXIMUM:
        hedgehog_info['Hunger'] = MOOD_MAXIMUM

    if hedgehog_info['Hunger'] < MOOD_MINIMUM:
        hedgehog_info['Hunger'] = MOOD_MINIMUM

    print(hedgehog_info)

    # Iterates through the aforementioned dictionary. This builds the
    # stats string for the status bar that reflects the criteria that
    # influences the hedgehog's mood.
    stats_str = ''
    for key, value in hedgehog_info.items():
        stats_str += key + ': ' + str(value) + '     '
    info_string.set(stats_str)

    enable_buttons()


def update_hedgehog_sayings(phrase):
    """
    This function updates the phrases used to reflect the hedgehog's
    feeling after every activity. The feelings displayed in the feedback
    bar represent direct feedback to the user.
    """
    print(phrase)
    hedgehog_sayings.set(phrase)


def main():
    # Layout initial hedgehog image in center frame.
    panel.pack(side=tk.BOTTOM, expand=True)

    # Layout status widget for top frame. The status bar is updated
    # with the criteria specified in the dictionary, this dictates the
    # hedgehog's mood
    info_label = tk.Label(top_frame,
                          font=("Helvetica", 16),
                          textvariable=info_string,
                          foreground="white",
                          background="orange",
                          )
    update_stats()
    info_label.pack()

    # Layout feedback widget for bottom frame. This feedback widget is
    # updated with various sayings reflecting what the hedgehog needs or
    # is feeling at a given time.
    message_label = tk.Label(btm_frame,
                             font=("Helvetica", 16),
                             textvariable=hedgehog_sayings,
                             foreground="white",
                             background="orange"
                             )
    update_hedgehog_sayings('Hello friend!')
    message_label.pack()

    # Layouts the exit button. Commands tkinter mainloop to exit.
    exit_button = tk.Button(ctr_right,
                            text="Exit \n👋",
                            font=("Helvetica", 16),
                            width=10,
                            height=3,
                            fg="orange",
                            command=window.quit)
    exit_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

    # Keeps tkinter window open until user quits.
    window.mainloop()
    print('Aloha friend!')


if __name__ == '__main__':
    main()
