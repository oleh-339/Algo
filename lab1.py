def longest_peak(numb):
    n = len(numb)
    max_length = 0

    if n < 3:
        return 0

    i = 1
    while i < n - 1:
        if numb[i - 1] < numb[i] > numb[i + 1]:
            left = i - 1
            right = i + 1

            while left > 0 and numb[left - 1] < numb[left]:
                left -= 1

            while right < n - 1 and numb[right] > numb[right + 1]:
                right += 1

            current_length = right - left + 1

            if current_length > max_length:
                max_length = current_length

        i += 1

    return max_length