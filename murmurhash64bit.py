def murmurhash64(key, seed=0):
    m = 0xc6a4a7935bd1e995
    r = 47
    h = seed ^ (len(key) * m)
    data = bytearray(key, "utf-8")

    def get_uint64(data, index):
        return ((data[index+7] << 56) | (data[index+6] << 48) | (data[index+5] << 40) |
                (data[index+4] << 32) | (data[index+3] << 24) | (data[index+2] << 16) |
                (data[index+1] << 8) | data[index])

    def fmix64(k):
        k ^= k >> r
        k = (k * 0x9c30d539) & 0xffffffffffffffff
        k ^= k >> r
        k = (k * 0x9c30d539) & 0xffffffffffffffff
        k ^= k >> r
        return k

    while len(data) >= 8:
        k = get_uint64(data, 0)
        k = (k * m) & 0xffffffffffffffff
        k ^= k >> r
        k = (k * m) & 0xffffffffffffffff

        h ^= k
        h = (h * m) & 0xffffffffffffffff

        data = data[8:]

    if len(data) >= 4:
        k = get_uint64(data, 0)
        k = (k * m) & 0xffffffffffffffff
        k ^= k >> r
        k = (k * m) & 0xffffffffffffffff
        h ^= k
        data = data[4:]

    if len(data) > 0:
        k = 0
        for i in range(len(data)):
            k |= (data[i] << (i * 8))
        k = (k * m) & 0xffffffffffffffff
        k ^= k >> r
        k = (k * m) & 0xffffffffffffffff
        h ^= k

    h ^= len(key)
    h = fmix64(h)

    return h
