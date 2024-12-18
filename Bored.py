import time
import sys
import os
import pygame

lirik_dengan_waktu = [
    ("Sticking for my name", 0.0, 2.5),
    ("And I'll keep you on my heart", 2.5, 7.0),
    ("Sticking through", 6.6, 2.5),
    ("Overnight", 7.5, 2.5),
    ("Everything", 11.5, 3.5),
    ("Is nothing more", 11.5, 3.0),
    ("Will he comeback to see you?", 14.5, 5.0),
    ("Thinking again", 18.5, 2.0),
    ("Will he comeback to save you?", 20.5, 3.0),
    ("Oh no", 23.5, 2.0),
    ("Take him away", 25.5, 3.0),
    ("Come to my life", 28.5, 3.5),
    ("I will give you all", 32.0, 4.0),
]

def jalanin_lirik():
    print("\nAnti Hero - Mighfar Suganda")
    time.sleep(2)

    for baris_lagu, waktu_mulai, durasi in lirik_dengan_waktu:
        while pygame.mixer.music.get_pos() < waktu_mulai * 1000:
            time.sleep(0.1)
        
        delay_karakter = durasi / len(baris_lagu)
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        print('')

if __name__ == "__main__":
    pygame.mixer.init()

    audio_path = "Mighfar Suganda - Anti ∞ Hero (Official Lyric Video) [07qofDUkU3s].mp3"

    if not os.path.exists(audio_path):
        print(f"Error: File audio '{audio_path}' tidak ditemukan.")
        sys.exit(1)

    try:
        pygame.mixer.music.load(audio_path)

        pygame.mixer.music.play()
        time.sleep(0.1)

        pygame.mixer.music.set_pos(160)

        jalanin_lirik()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Error memutar audio: {e}")
    finally:
        pygame.mixer.quit()
        print("\nCode By @Senofxs")
