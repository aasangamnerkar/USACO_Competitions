"""
ID: aasang1
LANG: PYTHON3
PROG: mooZ
"""

pp = input()
in_arr = [int(i) for i in pp.split(" ")]

in_arr.sort()
arr = [in_arr[0], in_arr[1], in_arr[-1]-in_arr[0]-in_arr[1]]
arr.sort()

print(arr[0], arr[1], arr[2])