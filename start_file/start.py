from subprocess import run


# At the first launch, dependencies are loaded, and only after that the game starts.
# On subsequent launches, the game starts immediately
def start_game():
    with open("./press_start.bat", 'w') as bat:
        with open("start_file/requirements.txt", 'r') as requirements:
            for command in requirements:
                print("loading...")
                run(command.split())
            bat.write("@echo off\ncolor 06\n@echo on\ncls\npython main.py")
    # with open("press_start.bat", 'r') as run_game:
    #     for command in run_game:
    #         print(command.split())
    #         print(1)
    #         run(command.split())
    run(["press_start.bat"])


start_game()
