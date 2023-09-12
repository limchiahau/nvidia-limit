#!/usr/bin/python3

import shutil
from pathlib import Path
import os


TIMER_FILE = "nvidia-tdp.timer"
SERVICE_FILE = "nvidia-tdp.service"
SYSTEMD_TIMER_DIR = Path("/etc/systemd/system")


def main():
    copy(TIMER_FILE, SYSTEMD_TIMER_DIR)
    copy(SERVICE_FILE, SYSTEMD_TIMER_DIR)

    configure_service()


def copy(filename, path):
    new_path = path / filename
    filename = Path(".") / filename

    shutil.copyfile(filename, new_path)


def configure_service():
    # stub
    pass


if __name__ == "__main__":
    print(os.getenv("USER"))

    main()
