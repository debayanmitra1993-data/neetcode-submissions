from typing import List, Set


def build_hash_set(keys: List[str]) -> Set[str]:
    myset = set()
    for k in keys:
        myset.add(k)
    return myset

def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    boollst = []
    for k in keys:
        if k in hash_set:
            boollst.append(True)
        else:
            boollst.append(False)
    return boollst

# do not modify below this line

output1 = build_hash_set(["Alice", "Bob", "Charlie"])
print(type(output1))         # check the type of the output
print(sorted(list(output1))) # set order is not guaranteed so we need to sort the list

output2 = build_hash_set(["XY", "XX", "YY", "XY", "YX"]) 
print(type(output2))         # check the type of the output
print(sorted(list(output2))) # set order is not guaranteed so we need to sort the list

print(check_keys({"Alice", "Bob", "Charlie"}, ["Alice", "Bob", "Charlie", "David"]))
print(check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']))
print(check_keys({'a', 'c'}, ['d', 'c']))
