def solve(lhs, rhs, var):
    try:
        counter = 0
        solved = False

        while not solved:
            lhs2 = ''
            rhs2 = ''

            for letter in lhs:
                if letter == var: lhs2 += str(counter)
                elif letter == '^': lhs2 += '**'
                else: lhs2 += letter

            for letter in rhs:
                if letter == var: rhs2 += str(counter)
                elif letter == '^': rhs2 += '**'
                else: rhs2 += letter

            if eval(lhs2) == eval(rhs2): solved = True; return counter
            counter += 1

    except:
        return 'error'