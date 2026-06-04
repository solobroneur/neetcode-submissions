class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        eating_speed = right

        while left <= right:
            k = (left + right) // 2

            total_eating_time = 0
            for pile in piles:
                total_eating_time += math.ceil(float(pile) / k)

            if total_eating_time <= h:
                eating_speed = k
                right = k - 1
            else:
                left = k + 1            

        return eating_speed
