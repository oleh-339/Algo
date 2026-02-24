def eeg_peaks(data):
    if not data:
        return 0, 0
    
    # пікове значення активності
    max_val = max(data)

    max_duration = 0
    current_duration = 0

    # проходимо по всьому масиву
    for value in data:
        if value == max_val:
            current_duration += 1
            if current_duration > max_duration:
                max_duration = current_duration
        else:
            current_duration = 0

    return max_duration, max_val