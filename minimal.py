arr = map(long, raw_input().split())

total = sum(arr)

min_sum = total - max(arr)
max_sum = total - min(arr)

print min_sum, max_sum
