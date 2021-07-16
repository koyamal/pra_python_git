sorted_s = ''.join(sorted(input()))
sorted_t = ''.join(sorted(input(), reverse=True))

if sorted_s < sorted_t:
    print('Yes')
else:
    print('No')
