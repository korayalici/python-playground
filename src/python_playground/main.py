def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()

def is_even(n: int) -> bool:
    return n % 2 == 0

def slugify(text: str) -> str:
    return text.lower().replace(" ", "-")
