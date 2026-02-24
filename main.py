from eeg import eeg_peaks

def main():
    try:
        # дані від користувача
        user_input = input("Введіть масив активності нейронів (ЧЕРЕЗ ПРОБІЛ): ")
        data = [float(x) for x in user_input.split()]

        # перевірка на пустий масив
        if not data:
            print("Помилка: Ви не ввели дані.")
            return

        duration, max_level = eeg_peaks(data)
        
        # результати аналізу
        print(f"Аналіз завершено:")
        print(f"- пікова активність: {max_level}")
        print(f"- протяжність цієї активності: {duration}")

    except ValueError:
        print("Помилка: Вводьте лише числа через пробіл.")

if __name__ == "__main__":
    main()