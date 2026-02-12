import re

def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()

def is_even(n: int) -> bool:
    return n % 2 == 0

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text