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
        print(f"list {x} sorted")
        return x

    if len(x) == 2 :
        print(f"Sorting x:{x} ...")
        a = x[0]
        b = x[1]
        if a > b :
            x[0] = b
            x[1] = a

        print(f"x sorted:{x}", end="\n\n")
        return x

    #meollo
    print(f"Divide and conquer...")
    first_half = x[:len(x)//2]
    second_half = x[len(x)//2:]
    print(f"x : {x} ---> {first_half} - {second_half}", end="\n\n")

    first_half_ordered = order(first_half)
    second_half_ordered = order(second_half)

    #merge ordered halfs
    print(f"\nMerging halfs {first_half_ordered} - {second_half_ordered} ...")
    x_ordered = []
    while len(first_half_ordered) > 0 :
        print(f"first_half_ordered: {first_half_ordered}, second_half_ordered: {second_half_ordered}")
        try :
            if first_half_ordered[0] <= second_half_ordered[0] :
                x_ordered.append(first_half_ordered.pop(0))
            if first_half_ordered[0] > second_half_ordered[0] :
                x_ordered.append(second_half_ordered.pop(0))
        except :
            x_ordered.append(first_half_ordered.pop(0))
    while len(first_half_ordered) > 0 :
        print(f"first_half_ordered: {first_half_ordered}, second_half_ordered: {second_half_ordered}")
        x_ordered.append(second_half_ordered.pop(0))
    print(f"I'm gonna return the following x_ordered: {x_ordered} to the next iteration of the program.")
    return x_ordered




    '''
    for i, j in first_half_ordered, second_half_ordered :
        if i < j :
            #x_ordered.append(first_half_ordered[i])
            print(f"i = {i}")
            next(i)
        if i > j :
            #x_ordered.append(second_half_ordered[j])
            print(f"j = {j}")
            next(j)
        else :
            x_ordered.append(i)
    '''

    


'''
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
'''



#x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#x = [1]
#x = [1, 2]
#x = []
x_ordered = order(x)

print(f"x_ordered = {x_ordered}. End of program.")
