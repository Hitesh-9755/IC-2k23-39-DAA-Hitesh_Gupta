"""
Longest Common Subsequence (LCS) - Dynamic Programming

Given two strings, find the length of the longest subsequence
present in both (not necessarily contiguous).

Uses a 2D DP table: dp[i][j] = LCS length of s1[:i] and s2[:j].
"""


def lcs(s1, s2):
    """Returns (lcs_length, lcs_string)."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtrack to recover the subsequence
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(result))


if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"

    length, subseq = lcs(s1, s2)
    print("String 1:", s1)
    print("String 2:", s2)
    print("LCS length:", length)
    print("LCS:", subseq)
