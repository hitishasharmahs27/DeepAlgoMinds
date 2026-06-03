class Solution:
    def numberOfPermutations(self, n, requirements):
        MOD = 10**9 + 7

        req = [-1] * n
        max_inv = 0

        for end, cnt in requirements:
            req[end] = cnt
            max_inv = max(max_inv, cnt)

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for length in range(1, n + 1):

            new_dp = [0] * (max_inv + 1)

            for inv in range(max_inv + 1):

                if dp[inv] == 0:
                    continue

                for add in range(length):

                    if inv + add <= max_inv:
                        new_dp[inv + add] = (
                            new_dp[inv + add] + dp[inv]
                        ) % MOD

            end_index = length - 1

            if req[end_index] != -1:

                required = req[end_index]

                filtered = [0] * (max_inv + 1)

                if required <= max_inv:
                    filtered[required] = new_dp[required]

                new_dp = filtered

            dp = new_dp

        return sum(dp) % MOD