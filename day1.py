# problem input is saved as 1.txt
# we open the input file as f
with open('1.txt') as f:
    # create a new list to store the calorie sums    
    sums = []
    # keep track of the current elf's calorie sum
    cur_sum = 0

    # iterate over each line in the input file
    for line in f:
        # get rid of the new line character
        line = line.strip()

        # if the string isn't empty, we have another value to read
        if line:
            # add the value to the current sum
            cur_sum += int(line)
        else:
            # the string was empty
            # append the most recent calorie sum to the list
            sums.append(cur_sum)
            # reset the sum counter
            cur_sum = 0
    # sort the list of calories in descending order
    sums.sort(reverse=True)

    # solve part 1 by finding the top
    print('Part 1:')
    print(sums[0])
    print('Part 2:')
    
    # solve part 2 by summing the top 3
    print(sum(sums[:3]))