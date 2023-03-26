def murmurhash32(key, seed=0):
    m = 0x5bd1e995
    r = 24
    h = seed ^ len(key)
    data = bytearray(key)

    while len(data) >= 4:
        k = data[0] | (data[1] << 8) | (data[2] << 16) | (data[3] << 24)
        k = (k * m) & 0xffffffff
        k ^= k >> r
        k = (k * m) & 0xffffffff

        h = (h * m) & 0xffffffff
        h ^= k

        data = data[4:]

    if len(data) == 3:
        h ^= data[2] << 16
    if len(data) >= 2:
        h ^= data[1] << 8
    if len(data) >= 1:
        h ^= data[0]
        h = (h * m) & 0xffffffff

    h ^= h >> 13
    h = (h * m) & 0xffffffff
    h ^= h >> 15

    return h
