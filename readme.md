# nvidia-limit

The purpose of this script is to set the power limit of my nvidia gpu.
The power limit will be set each time the pc is turned on.

The power limit of this script is 140 Watts.

## Usage

To use this script you need to cd to this project's root directory.

Make *main.py* executable.

    chmod +x main.py

Then run the script with administrative rights.

    sudo ./main.py


## Notes
Administrative rights are required to place the files in the rights places and
use the *systemctl* command.