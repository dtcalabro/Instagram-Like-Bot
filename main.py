"""
Instagram bot

Note:   
    This is a proof of concept project and I don't endorse liking bots for Instagram. This was purely for learning and if you 
    have an issue with the posting of this project, contact me and we can talk about taking it down.

This code does what I wanted it to do, so I am stopping here. Plenty more could be done, but this is just a proof of concept 
so I'm done working on it.
"""

from instagram_bot_simplified import instagram_bot
import json

# Calling the config file.
config_json = "/Users/yourname/Desktop/Python_Projects/Instagram_Bot_Final/config.json"

# Main loop
def mainloop():
    # Opening the config file so we can declare all the variables.
    if __name__ == "__main__":
        with open(config_json) as file:
            config = json.load(file)

        # Below we declare all our variables so that we can later call them.
        driver = config["driver"]
        url = config["url"]
        posturl = config["posturl"]
        username = config["username"]
        password = config["password"]
        username1 = config["username1"]
        password1 = config["password1"]
        username2 = config["username2"]
        password2 = config["password2"]
        username3 = config["username3"]
        password3 = config["password3"]
        username4 = config["username4"]
        password4 = config["password4"]
        username5 = config["username5"]
        password5 = config["password5"]
        # If you decide to add more accounts, then follow the format above and declare them in the next few lines below.
        """

        Add extra accounts here, and make sure to uncomment it so that it can be read by the computer.

        """
        
        # The next part is where we call the functions needed for the accounts to do their thing.
        # These functions below are defined in the instagram_bot_simplified.py file, so all we have to do is call them.
        # 1st Account
        ig = instagram_bot(driver, url, username, password)
        ig.go_to_post(posturl)
        ig.like_post()
        ig.close_window()
        # 2nd Account
        ig2 = instagram_bot(driver, url, username1, password1)
        ig2.go_to_post(posturl)
        ig2.like_post()
        ig2.close_window()
        # 3rd Account
        ig3 = instagram_bot(driver, url, username2, password2)
        ig3.go_to_post(posturl)
        ig3.like_post()
        ig3.close_window()
        # 4th Account
        ig4 = instagram_bot(driver, url, username3, password3)
        ig4.go_to_post(posturl)
        ig4.like_post()
        ig4.close_window()
        # 5th Account
        ig5 = instagram_bot(driver, url, username4, password4)
        ig5.go_to_post(posturl)
        ig5.like_post()
        ig5.close_window()
        # 6th Account
        ig6 = instagram_bot(driver, url, username5, password5)
        ig6.go_to_post(posturl)
        ig6.like_post()
        ig6.close_window()
        # If you decide to add more accounts, then follow the format above and call them in the next few lines below.
        """

        Call extra accounts here, and make sure to uncomment it so that it can be read by the computer.

        """

# We have to call the main loop so it will execute.
mainloop()
