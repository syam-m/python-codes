def solve(k2, k3, k5, k6):

    count_256 = min(k2, k5, k6)
    k2 -= count_256

    count_32 = 0
    if k2 > 0:
        count_32 = min(k2, k3)

    return (count_32 * 32) + (count_256 * 256)


if __name__ == "__main__":

    k2, k3, k5, k6 = map(int, raw_input().split(" "))
    print solve(k2, k3, k5, k6 )
