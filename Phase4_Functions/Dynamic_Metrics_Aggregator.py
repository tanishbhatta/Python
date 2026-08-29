def aggregate_metrics(*args):
    #Sum
    total_sum = 0
    for i in args:
        total_sum += i

    #Average
    average = total_sum/len(args)

    #Minimum
    minimum = args[0]
    for i in args:
        if i < minimum:
            minimum = i
    
    #Maximum
    maximum = args[0]
    for i in args:
        if i > maximum:
            maximum = i
    
    return total_sum, average, minimum, maximum

print(aggregate_metrics(10, 20, 30, 40))

        
    
    
    

