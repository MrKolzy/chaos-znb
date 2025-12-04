from Window import Window

def main() -> int:
    try:
        window = Window("Chaos Zero Nightmare")
        window.bring_to_foreground()
    except Exception as exception:
        print(f"[Exception]: {exception}")

    return 0

if __name__ == "__main__":
    main()