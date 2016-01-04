# The main idea of this algorithm is to replace ')' to '0' and '(' to '1', allowing to treat
# any combination of brackets as a binary number.
# It goes over all the possible combinations of parentheses(binary numbers),
# with N * 2 digits.
# Conditions when combination is "true parentheses expression":
# when iterating through the expression from left to right
# every opened parenthesis '(' must be closed by ')'
# and the number of '(' and ')' must be equal.

N = int(input("How many opening parentheses (or closing, if you like) you want?\n"))
while(N <= 0):
    print ("Bad input!")
    N = int(input("Input number of parentheses again:\n"))

#start expression will be like
#100***000 what is equal to
#())***)))
START = 2 ** (2 * N - 1)

#and the end will be like
#111***111 what is equal to
#(((***(((
END = 2 ** (2 * N) - 1

sum_of_right_expressions = 0
for i in range(START, END + 1):
    num_of_opened_parentheses = 0

    #next parentheses expression in binary form (example: 0b10101100)
    #                                                       ()()(())
    current = list(bin(i))

    #delete '0b' from the begin of our expression
    del current[0]
    del current[0]

    #core of algorithm
    for j in range(len(current)):
        if num_of_opened_parentheses < 0:
            break
        if current[j] == '1':
            num_of_opened_parentheses += 1
            continue
        if current[j] == '0':
            num_of_opened_parentheses -= 1
            continue
    #current expression is
    if(num_of_opened_parentheses == 0):
        sum_of_right_expressions += 1

        for j in range(len(current)):
            if current[j] == '0':
                print (')', end = '')
                continue
            else:
                print ('(', end = '')
        print ()

print ("There are ", sum_of_right_expressions, " correct expressions.")