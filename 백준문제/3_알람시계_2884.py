H, M = input().split()
H = int(H)
M = int(M)
fast_time = H * 60 + M - 45
if fast_time < 0:
    fast_time = (H+24) * 60 + M - 45
    fast_time_H = fast_time // 60
    fast_time_M = fast_time % 60
else:
    fast_time_H = fast_time // 60
    fast_time_M = fast_time % 60

print(fast_time_H, fast_time_M)
