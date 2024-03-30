def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    for num in range(start, stop + 1):
        print(num)
    

print('should print 5 6 7 below')        
count_up(5, 7)

print('should print 0 1 2 3 4 5 6 7 8 below')        
count_up(0, 8)
