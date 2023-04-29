class Solution:
    def countBits(self, n: int) -> list[int]:
        ls = []
        for i in range(n + 1):
            # bit = int(bin(i)[2:])
            bit_sum = sum([int(bit) for bit in bin(i)[2:]])
            ls.append(bit_sum)

        print(ls)


sol = Solution()

sol.countBits(5)
