def order(x: list) -> list:
    #type check
    if type(x) != type([]) :
        print("This function requires a list as its argument")
        raise SystemExit

    #corner cases
    if len(x) == 0:
        print("Empty list")
        raise SystemExit

    if len(x) == 1 :
        return x

    if len(x) == 2 :
        a = x[0]
        b = x[1]
        if a > b :
            x[0] = b
            x[1] = a
        return x

    #divide and conquer
    first_half = x[:len(x)//2]
    second_half = x[len(x)//2:]

    first_half_ordered = order(first_half)
    second_half_ordered = order(second_half)

    #merge ordered halfs
    x_ordered = []
    while len(first_half_ordered) > 0 :
        try :
            if first_half_ordered[0] <= second_half_ordered[0] :
                x_ordered.append(first_half_ordered.pop(0))
            else :
                x_ordered.append(second_half_ordered.pop(0))
        except :
            x_ordered.append(first_half_ordered.pop(0))
    while len(second_half_ordered) > 0 :
        x_ordered.append(second_half_ordered.pop(0))
        
    #return sorted list
    return x_ordered



x = [1, 2]
x = []
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [9, 8, 7, 6, 5, 4, 3, 2, 1]


x_ordered = order(x)
print(f"{x} --> {x_ordered}")
