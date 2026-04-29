class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slst = list(s)
        tlst = list(t)
        ds = {}
        dt = {}
        # lets check edge case, if we see that slst and tlst are different lengths, we can just return False
        if len(tlst) != len(slst):
            return False
        # now we just iterate through each list and add key and values to each dictionary,
        # incrementing value based on the amount of occurances we see of each character
        for i in range(len(tlst)):
            # check if character key is in dictionary, if not we create an entry (start at 0 for this implementation)
            if slst[i] not in ds:
                ds[slst[i]] = 0
            if tlst[i] not in dt:
                dt[tlst[i]] = 0
            # then whether or not its a new key or an old key, since we see it at this iteration, we increment the value of the key by 1
            ds[slst[i]] += 1
            dt[tlst[i]] += 1
        # after iterating through both lists, we just return a comparison of ds and dt, which if they're the same key-value pairs,
        # we will see our function return True, else False, since same key-value pairs implies anagram (same number of chars in both strings)
        return ds == dt