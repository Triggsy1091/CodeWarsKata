def nb_year(p0, percent, aug, p):
    # your code
    # intialise n - number of full years for p0 to equal or exceed p
    n = 0
    # convert percent to percentage
    percentage = percent / 100
    
    # use while loop to determine if p0 is still less than p
    while p0 < p:
        # p0 multiplied by percentage and add aug
        p0 += (p0 * percentage) + aug
        n += 1
    return n

nb_year(1500, 5, 100, 5000)