
# CPSC 335 - Project 3
# Problem 2: Longest Common Subsequence
# Dyllan Cummings

def longest_common_subsequence(text1, text2):
    n = len(text1)
    m = len(text2)

    # Create a DP table initialized to zero.
    T = [[0 for j in range(m + 1)] for i in range(n + 1)]

    # Fill the table using previously calculated values.
    for i in range(1, n + 1):
        for j in range(1, m + 1):

            # Matching characters extend the LCS by one.
            if text1[i - 1] == text2[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1

            # Otherwise, take the better of two subproblems.
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    # Bottom-right cell contains the LCS length.
    return T[n][m]


def main():
    print("Example 1:")
    print(longest_common_subsequence("algorithm", "rhythm"))

    print("Example 2:")
    print(longest_common_subsequence("sort", "sport"))

    print("Example 3:")
    print(longest_common_subsequence("dynamic", "program"))


if __name__ == "__main__":
    main()
