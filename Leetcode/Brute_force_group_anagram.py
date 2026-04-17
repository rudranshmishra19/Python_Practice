from typing import List
class solution:
    def groupAnagrams(self,strs: List[str])->list[list[str]]:
        # List containing result
        result=[]
        # tracking list
        used=[False]*len(strs)
        # Loop till the end of list str
        for i in range(len(strs)):
            if used[i]:
                continue
            current_group=[strs[i]]
            used[i]=True  #assign used as True
            sorted_current=''.join(sorted(strs[i]))

            for j in range(len(strs)):
                if used[j]:
                    continue
                # Sorted the other word and compare
                sorted_other=''.join(sorted(strs[j]))
                
                if sorted_current==sorted_other:
                    current_group.append(strs[j])
                    used[j]=True

            result.append(current_group)
        return result
                

sol=solution()
print(sol.groupAnagrams(["eat","bat","tea"]))