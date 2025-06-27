






def order(x: list) -> list:
    first_half = x[:len(x)//2]
    second_half = x[len(x)//2:]

    for i in range(len(first_half) - 1) :
        if first_half[i] < first_half[i+1] :
            print(first_half, "<", second_half)
            i+1
            if i == range(i) :
                exit()
            continue
        else :
            print(f"{first_half} < {second_half}. We proceed to order first_half")
            order(first_half)


    print(first_half, second_half)

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
order(x)

print("end of program")