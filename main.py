import os
import random

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def play_music(folder, song):
    file_path = os.path.join(folder, song)

    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print(f"\nNow playing '{song}'")
    print("Options: [P]ause, [R]esume, [S]top")

    while True:
        options = input("> ").upper()
        if options == "P":
            pygame.mixer.music.pause()
            print("Paused")
        elif options == "R":
            pygame.mixer.music.unpause()
            print("Resumed")
        elif options == "S":
            pygame.mixer.music.stop()
            print("Stopped")
            return
        else:
            print("Invalid option")


def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio initialization failed", e)
        return

    current_dir = os.path.dirname(os.path.abspath(__file__))
    ignore_folders = {".idea", ".venv"}

    folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f)) and f not in ignore_folders]

    if not folders:
        print("No folders found in the current directory.")
        exit(0)

    if len(folders) == 1:
        folder_name = folders[0]
        print(f"Opening folder '{folder_name}' ...")
    else:
        print("Select a folder:")
        for index, folder in enumerate(folders, start=1):
            print(f"{index}. {folder}")

        while True:
            folder_choice = input("Enter folder number: ")
            if folder_choice.isdigit() and 1 <= int(folder_choice) <= len(folders):
                folder_name = folders[int(folder_choice) - 1]
                break
            else:
                print("Invalid choice. Enter a valid number")

    songs = [file for file in os.listdir(folder_name) if file.endswith(".mp3")]

    if not songs:
        print("No songs found")
        return

    while True:
        print("***** Music Player *****")
        print("My song list:")
        for index, song in enumerate(songs, start=1):
            print(f"{index}. {song}")

        choice = input("Enter your choice, 'SH' shuffle play or 'Q' to quit: ")
        if choice.upper() == "Q":
            print("Exiting...")
            break

        if choice.upper() == "SH":
            random_song = random.choice(songs)
            play_music(folder_name, random_song)
            continue

        if not choice.isdigit():
            print("Invalid choice. Enter a valid number")
            continue

        choice = int(choice) - 1

        if 0 <= choice < len(songs):
            play_music(folder_name, songs[choice])
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
