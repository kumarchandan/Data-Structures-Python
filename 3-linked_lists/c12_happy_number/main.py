def find_happy_number(num):
    # TODO: Write your code here
    happy_number = False
    sum_so_far = []
    while num:
        # happy number
        inner_num = num
        sum = 0
        while inner_num:
            sum = sum + (inner_num % 10) ** 2
            inner_num = inner_num // 10
        # break condition 1 - happy number
        if sum == 1:
            happy_number = True
            break
        # break condition 2 - not a happy number
        if sum in sum_so_far:
            happy_number = False
            break
        sum_so_far.append(sum)
        num = sum
    return happy_number


def main():
#   print(find_happy_number(23))
    print(find_happy_number(12))

main()
