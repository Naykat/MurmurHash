import struct

def murmurhash128(key, seed=0):
    m = 0x5bd1e9955bd1e9955bd1e9955bd1e995
    r = 31
    h1 = seed
    h2 = seed
    data = bytearray(key, "utf-8")

    def get_uint64(data, index):
        return ((data[index+7] << 56) | (data[index+6] << 48) | (data[index+5] << 40) |
                (data[index+4] << 32) | (data[index+3] << 24) | (data[index+2] << 16) |
                (data[index+1] << 8) | data[index])

    def fmix64(k):
        k ^= k >> 33
        k = (k * 0xff51afd7ed558ccd) & 0xffffffffffffffff
        k ^= k >> 33
        k = (k * 0xc4ceb9fe1a85ec53) & 0xffffffffffffffff
        k ^= k >> 33
        return k

    while len(data) >= 16:
        k1 = get_uint64(data, 0)
        k1 = (k1 * m) & 0xffffffffffffffff
        k1 ^= k1 >> r
        k1 = (k1 * m) & 0xffffffffffffffff

        h1 ^= k1
        h1 = (h1 * m) & 0xffffffffffffffff

        k2 = get_uint64(data, 8)
        k2 = (k2 * m) & 0xffffffffffffffff
        k2 ^= k2 >> r
        k2 = (k2 * m) & 0xffffffffffffffff

        h2 ^= k2
        h2 = (h2 * m) & 0xffffffffffffffff

        data = data[16:]

    if len(data) >= 8:
        k1 = get_uint64(data, 0)
        k1 = (k1 * m) & 0xffffffffffffffff
        k1 ^= k1 >> r
        k1 = (k1 * m) & 0xffffffffffffffff
        h1 ^= k1
        data = data[8:]

    if len(data) >= 4:
        k2 = struct.unpack('<I', data[:4])[0]
        k2 = (k2 * m) & 0xffffffff
        k2 ^= k2 >> r
        k2 = (k2 * m) & 0xffffffff
        h2 ^= k2
        data = data[4:]

    if len(data) > 0:
        k3 = 0
        for i in range(len(data)):
            k3 |= (data[i] << (i * 8))
        k3 = (k3 * m) & 0xffffffffffffffff
        k3 ^= k3 >> r
        k3 = (k3 * m) & 0xffffffffffffffff
        h1 ^= k3

    h1 ^= len(key)
    h2 ^= len(key)

    h1 += h2
    h2 += h1

    h1 = fmix64(h1)
    h2 = fmix64(h2)

    h1 += h2
    h2 += h1

    return (h1, h2)
