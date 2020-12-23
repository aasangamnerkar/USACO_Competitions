"""
ID: aasang1
LANG: PYTHON3
PROG: petals
"""

N = int(input())
pp = input()
in_arr = [int(i) for i in pp.split(" ")]

def recurse(arr, temp_arr, index, s):
    if index < N:
        for i, item in enumerate(arr[index:]):
            temp_arr.append(item)
            avg = sum(temp_arr)/len(temp_arr)
            if avg % 1 == 0.0:
                if avg in temp_arr:
                    s += 1
        return recurse(arr, [], index+1, s)
    else:
        return s

print(recurse(in_arr, [], 0, 0))