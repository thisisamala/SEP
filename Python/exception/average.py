def average():
    try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        sum = 0
        count = 0

        for num in numbers:
            sum += num
            count += 1

        if count == 0:
            raise TypeError("YOU HAVE TO PUT ELEMENTS IN THE LIST")

        avg = sum / count
        print(avg)

    except ValueError:
        print("Please enter valid integers.")
    except TypeError as e:
        print(e)

average()
