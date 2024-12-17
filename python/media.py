"""sacar media entre dos jugadores"""
kim = [9.8, 10.4, 10.5, 9.3, 9.7, 8.5, 7.8, 9.2, 9.4, 9.4]
yusuf = [9.0, 10.3, 10.2, 10.6, 10.9, 9.2, 8.5, 9.6, 8.9, 8.7]

def mean(numbers):
    return sum(numbers) / len(numbers)

kim_mean = mean(kim)
yusuf_mean = mean(yusuf)

print(f"Media Kim {kim_mean:.1f}")
print(f"Media Yusuf {yusuf_mean:.1f}")


