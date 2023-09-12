TIMER_FILE = "nvidia-tdp.timer"
SERVICE_FILE = "nvidia-tdp.service "
SYSTEMD_TIMER_DIR = r"/etc/systemd/system"


def main():
    copy(TIMER_FILE, SYSTEMD_TIMER_DIR)
    copy(SERVICE_FILE, SYSTEMD_TIMER_DIR)

    configure_service()


def copy(filename, path):
    # stub
    pass


def configure_service():
    # stub
    pass


if __name__ == "__main__":
    main()
