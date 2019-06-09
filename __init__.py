from srv.twitchSrv import twitchStart

def menu():
    print("MAIN MENU")
    print("-"*20)
    print("1. Begin Twitch Bot")
    print("2. Begin Discord Bot")
    print("3. Begin Twitch and Discord Seperate Bots")
    print("4. Begin Twitch and Discord linked Bot")
    print("-"*20)
    menu_choices = {"1": 1, "2": 2, "3": 3, "4": 4}
    menu_choice = input("Enter what you want to do:")
    if menu_choices[menu_choice] == 1:
        twitchStart()
    if menu_choices[menu_choice] == 2:
        print("2")
    if menu_choices[menu_choice] == 3:
        print("3")
    if menu_choices[menu_choice] == 4:
        print("4")

menu()
    