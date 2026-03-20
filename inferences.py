import pandas as pd
import pytchat


video_id = "6lC4wrcWAm4"

def main():
    chat = pytchat.create(video_id)

    try:
        while chat.is_alive():
            # TBA

    except:
        print("Error: Video ID tidak valid")
        # TBA

if __name__ == "__main__":
    print(f"Youtube Inferences dimulai")
    print("===========Harap tunggu sampai selesai===========")
    main()

# Belum selesai breeee