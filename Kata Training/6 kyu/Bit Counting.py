def count_bits(n):
    sum = 0
    for i in str((bin(n)))[2:]:
        sum += int(i)
    return sum
