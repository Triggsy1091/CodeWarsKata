def delete_nth(order,max_e):
    reduced_list = []
    count = {}
    for num in order:
        if num in count and count[num] < max_e:
            reduced_list.append(num)
            count[num] += 1
        elif num not in count:
            reduced_list.append(num)
            count.update({num: 1})
    return reduced_list

delete_nth([20,37,20,21], 1) # [20,37,21])
delete_nth([1,1,3,3,7,2,2,2,2], 3) # [1, 1, 3, 3, 7, 2, 2, 2])