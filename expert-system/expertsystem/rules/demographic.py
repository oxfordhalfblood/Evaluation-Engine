# userinputFunct = '5*(1-(x*1))'

def accountlife(accountid):
    accountlife = 32
    return accountlife


def latest_ad_life(accountid):
    latest_ad_life = 37
    return latest_ad_life

def checkage(age):
    try:
        if age>15 & age<50:
            print("ad performing well")
        else:
            print("ad performance below average")

    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...", e)
        raise

def display(args):
    # if len(args) > 1:
    #     raise TypeError('dis() takes 1 argument ({} given)'.format(len(args) + 1))
    print(args)
    return args

