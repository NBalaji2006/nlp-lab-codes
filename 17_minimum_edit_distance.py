"""Compute unit-cost minimum edit distance between two strings."""


def edit_distance(source: str, target: str) -> tuple[int, list[list[int]]]:
    rows, columns = len(source) + 1, len(target) + 1
    dp = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        dp[i][0] = i
    for j in range(columns):
        dp[0][j] = j
    for i in range(1, rows):
        for j in range(1, columns):
            substitution_cost = 0 if source[i - 1] == target[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + substitution_cost,
            )
    return dp[-1][-1], dp


def main() -> None:
    source = input("Source string: ")
    target = input("Target string: ")
    distance, table = edit_distance(source, target)
    print(f"Minimum edit distance: {distance}")
    for row in table:
        print(row)


if __name__ == "__main__":
    main()
