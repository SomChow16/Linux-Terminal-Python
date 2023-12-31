print("Welcome to a Basic Linux terminal emulator python project developed by Somnath Chowdhury a 16 year old junipr highschool student")
print("* Commands that will only run - ls, cd, mv, history, exit")
print("* Other commands are still in development or may not be available, just be satisfied")

file_syst = {
    'c': [
        'Recycle.Bin',
        'ProgramData',
        'hiberfil.sys',
        'WinREAgent',
        'New folder',
        'Recovery',
        'Program Files',
        'python-3.11.4-amd64.exe',
        'Intel',
        'Program Files (x86)',
        'Windows'
    ],
    'User': {
        'Downloads': {
            "Files": [
                "asd.mp3",
                "qwert.jpeg",
                "winar.exe"
            ],
            "Music": [
                "song1.mp3",
                "song2.mp3"
            ]
        },
        'Desktop': [
            'Microsoft Edge.lnk',
            'Microsoft Office Excel 2007.lnk',
            'Microsoft Office Word 2007.lnk'
        ],
        'Documents': [
            "fghj.pdf",
            'asdsd.docx'
        ],
        'Favorites': [
            "Links",
            "desktop.ini"
        ]
    }
}

current_directory = 'c'  # Initialize the current directory

commands = []

while True:
    command = input(f"LinuxUser@DESKTOP-U56C2OD:{current_directory}$ ")
    commands.append(command)

    if command.startswith('cd'):
        parts = command.split()
        if len(parts) == 1:
            # If 'cd' is entered without a target directory, return to 'c' drive
            current_directory = 'c'
        else:
            target_directory = parts[-1]
            current_directory = target_directory  # Update the current directory

    elif command.startswith('ls'):
        # List available directories or files in the current directory
        if current_directory in file_syst:
            for item in file_syst[current_directory]:
                print(item)
        elif current_directory in file_syst['User']:
            for val in file_syst['User'][current_directory]:
                print(val)

        elif command == 'ls Downloads/Music':
            # List songs in the Music directory under Downloads
            print(" ".join(file_syst['User']['Downloads']["Music"]))
        elif command == 'ls Downloads/Files':
            # List files in the Files directory under Downloads
            print(" ".join(file_syst['User']['Downloads']["Files"]))
        elif command == 'ls Desktop':
            # List files in the Favorites directory
            print(" ".join(file_syst['User']['Desktop']))
        elif command == 'ls Favorites':
            # List files in the Favorites directory
            print(" ".join(file_syst['User']['Favorites']))
        elif command == 'ls c':
            # List files in the c directory
            print(" ".join(file_syst['c']))
        else:
            # Placeholder for handling other commands related to changing directories
            print("Error: Unrecognized command")

    elif command.startswith('mv'):
        move_command = command[3:]   # slice the string right after 'mv'
        parts = move_command.split()  #after slicing out the 'mv', it will split the strings into 3 parts


        if len(parts) == 3:
            src_dir_name, targ_dir_name, file_name = parts   # assign the 3 parts of the string after splitting to variables
            src_dir_name = src_dir_name.title()   # convert to title case to match dictionary keys

            if src_dir_name in file_syst['User'] and targ_dir_name in file_syst['User']:
                src_dir = file_syst['User'][src_dir_name]
                targ_dir_name = targ_dir_name.title()

                if file_name in src_dir:
                    src_dir.remove(file_name)
                    file_syst['User'][targ_dir_name].append(file_name)
                    print(f"{file_name} moved to {targ_dir_name}")
                else:
                    print(f"Error: {file_name} not found in {src_dir_name}")
            else:
                print("Error: Source directory or destination directory not found")
        else:
            print("Invalid move command")
    elif command.startswith('history'):
           for cmd in commands:
               print(cmd)


    elif command.startswith('exit'):
        print("Logging out")
        break

    else:
        print("Error: Unrecognized command")
