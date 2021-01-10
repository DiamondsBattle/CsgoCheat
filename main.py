from plugins import glow

def main():
    settings = {glow.Glow: True}

    for i in settings:
        if settings[i]:
            i()


if __name__ == '__main__':
    main()