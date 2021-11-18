def mul(num1, num2):
    sum = 0

    for i in reversed(range(len(num1))):
        reversedInx1 = (len(num1) - i - 1)
        n1 = int(num1[i]) * (10 ** reversedInx1)

        for j in reversed(range(len(num2))):
            reversedInx2 = (len(num2) - j - 1)
            n2 = int(num2[j]) * (10 ** reversedInx2)
            sum += n1 * n2

    return str(sum)
