from calclib import Advanced

math = Advanced()


def calculate_deviation(nums: list):
    N = len(nums)
    sum = 0
    mean = calculate_mean(nums)

    for i in range(0, N):
        sum = math.add(sum, math.power(int(nums[i]), 2))

    const = math.mul(N, math.power(mean, 2))
    res = math.rootn(2, math.div(math.sub(sum, const), math.sub(N, 1)))
    return res


def calculate_mean(nums: list):
    N = len(nums)
    x = 0
    for i in range(0, N):
        x = math.add(x, int(nums[i]))

    return math.mul(math.div(1, N), x)


if __name__ == '__main__':
    nums = input().split(" ")
    print(calculate_deviation(nums))