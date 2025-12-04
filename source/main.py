from window import Window

def main() -> int:
    try:
        Window("Chaos Zero Nightmare")
    except Exception as exception:
        print(f"[Exception]: {exception}")

    return 0

if __name__ == "__main__":
    main()