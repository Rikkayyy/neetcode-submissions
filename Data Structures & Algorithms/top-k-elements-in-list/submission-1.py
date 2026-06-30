class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq_buckets[c].append(n)

        groups = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for num in freq_buckets[i]:
                groups.append(num)
                if len(groups) == k:
                    return groups
