import pandas as pd # not yet being used dumbass (belum kepake)
import pytchat
import json

# https://www.youtube.com/watch?v=ZLk2NqvCOrw
"""
    Marapthon live
"""
video_id = "ZLk2NqvCOrw"

def main():
    chat = pytchat.create(video_id)

    try:
        while chat.is_alive():
            # TBA
            for c in chat.get().sync_items():
                # print(f"{c.datetime} [{c.author.name}]- {c.message}")
                livechat_obj = c.json()
                live_chat = json.loads(livechat_obj)
                
                print(live_chat['datetime'] + " : " + live_chat['author']['name'] + " : " + live_chat['message'])

    except Exception as error:
        print(f"Error: {error}")
        # TBA

if __name__ == "__main__":
    print(f"Youtube Inferences dimulai")
    print("===========Harap tunggu sampai selesai===========")
    main()
    exit()

# Belum selesai breeee

