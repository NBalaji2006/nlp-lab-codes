"""Check for exactly two 19s and at least three 5s in a list of integers."""


def valid_list(values: list[int]) -> bool:
    return values.count(19) == 2 and values.count(5) >= 3


def main() -> None:
    values = [int(value) for value in input("Enter integers separated by spaces: ").split()]
    print(valid_list(values))


if __name__ == "__main__":
    main()
