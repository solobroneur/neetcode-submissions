class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert array to max heap / priority queue
        heapq.heapify_max(stones)

        # Percolate & compare until no more than 1 stone
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, x - y)
            
        # Add 0 if none are left
        stones.append(0)
        return stones[0]
        