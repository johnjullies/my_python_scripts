def allowance_calculator(cost_per_day, days):
    allowance = cost_per_day * days

    print 'Allowance: %s' % (allowance)

def main():
    cost_per_day = input('How much is the cost per day? ')
    days = input('For how many days? ')

    allowance_calculator(cost_per_day, days)

if __name__ == '__main__':
    main()
