def square_root_bisection(num, tolerance=0.0001, max_ite=20):
    if num < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif num == 0 or num == 1:
        print(f'The square root of {num} is {num}')
        return num

    low = 0
    high = max(1, num)
    for _ in range(max_ite):
        mid = (low + high) / 2
        square = mid * mid
        if (high - low) / 2 < tolerance:
            print(f"The square root of {num} is approximately {mid}")
            return mid
        if square < num:
            low = mid
        else:
            high = mid

    print(f"The square root of {num} is approximately {mid}")
    print(f"Failed to converge within {max_ite} iterations")
    return None

