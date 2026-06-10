class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent_nums = {}
        for item in nums:
            if item in most_frequent_nums.keys():
                most_frequent_nums[item] += 1
            else:
                most_frequent_nums[item] = 1
        most_frequent_nums = dict(sorted(most_frequent_nums.items(), key = lambda item: item[1], reverse = True))
        top_nums = []
        for i, (key, value) in enumerate(most_frequent_nums.items()):
            if i == k:
                break
            top_nums.append(key)
        return top_nums

