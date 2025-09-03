passkey = [
    ['q', 'w', 'e', 'r', 't', 'y'],
    ['u', 'i', 'o', 'p', 'a', 's'],
    ['d', 'f', 'g', 'h', 'j', 'k'],
    ['x', 'c', 'v', 'b', 'n', 'm']
]

a = input()
for i in range(0, len(a), 2):
    row = int(a[i])
    col = int(a[i + 1])
    print(passkey[row][col], end='')
