def make_div_by(n):
    '''This closure returns a function that returns the
        division of an x number by n
    '''
    def div_by(x):
        return x / n
    return div_by


div_by_3 = make_div_by(3)
print(div_by_3(18))  # 6

div_by_5 = make_div_by(5)
print(div_by_5(100))  # 20

div_by_18 = make_div_by(18)
print(div_by_18(54))  # 3