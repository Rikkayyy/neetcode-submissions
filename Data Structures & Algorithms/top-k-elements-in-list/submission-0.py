class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq_buckets = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = count.get(number, 0) + 1
        
        for num, freq in count.items():
            freq_buckets[freq].append(num)

        result = []
        for i in range(len(freq_buckets) - 1, 0, -1):
            for n in freq_buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result