"""Prints a spelled-out hello world message."""


def spell_out(message: str) -> str:
    letters = [char for char in message if char != " "]
    return " ".join(letters)


def main() -> None:
    message = "Hello World"
    print(spell_out(message))


if __name__ == "__main__":
    main()
