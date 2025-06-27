def order(x: list) -> list:
    if len(x) == 2 :
        print(f"Sorting x:{x}")
        a = x[0]
        b = x[1]
        if a > b :
            x[0] = b
            x[1] = a
            print(f"x sorted:{x}")
        

    if len(x) == 1 :
        print(f"list {x} sorted")
        quit()

    first_half = x[:len(x)//2]
    second_half = x[len(x)//2:]

    if len(first_half) == 2 :
        order(first_half)
        order(second_half)

    if len(first_half) > 2 :
        for i in range(len(first_half) - 1) :
            if first_half[i] < first_half[i+1] :
                print(first_half[i], "<", first_half[i+1])
                i+1
                if i == len(range(i) - 1) :
                    order(second_half)
                continue
            else :
                print(f"first_half = {first_half}")
                print(f"{first_half[i]} > {first_half[i+1]}.\nWe proceed to order first_half\n")
                order(first_half)



#x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#x = [1]
order(x)

print("end of program")
