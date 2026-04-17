from collections import defaultdict
from typing import List
class solution:
    def groupAnagram(self,strs:List[str])->List[List[str]]:
        group_anagram=defaultdict(list)
        # loop till the end of strs
        for s in strs:
            key=''.join(sorted(s))
            group_anagram[key].append(s)
        return list(group_anagram.values())

sol=solution()
print(sol.groupAnagram(["eat","meat","seat","taes","tea"]))
      


        
