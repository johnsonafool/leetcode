from typing import List, Optional


class Solution:
    def checkStraightLine(coordinates: List[List[int]]) -> bool:
        # delta_x =
        # delta_y = coordinates[-1][1] - coordinates[0][1]
        slope = (
            coordinates[-1][1]
            - coordinates[0][1] / coordinates[-1][0]
            - coordinates[0][0]
        )

        print(slope)

        for i in range(len(coordinates) - 1):
            if (coordinates[i + 1][1] - coordinates[i][1]) / (
                coordinates[i + 1][0] - coordinates[i][0]
            ) != slope:
                return False
        return True


solve = Solution.checkStraightLine(
    coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
)
