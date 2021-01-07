'''range functions'''

# pylint: disable=E0401, E1101, E1601, W0612

stackPotCutoffs = {
    'low': 200,
    'mid': 1000,
    'high': 2000
}

stackPotScalers = {
    'low': 10,
    'mid': 50,
    'high': 100
}

potRateCutoffs = {
    'low': 2,
    'mid': 4
}

potRateScalers = {
    'low': 0.2,
    'mid': 0.5
}

def range_stack(stack, small_blind_amount):
    '''create ranges from stack'''

    stack = stack / small_blind_amount
    if stack < stackPotCutoffs['low']:
        rng = str(int(stack / stackPotScalers['low']) * stackPotScalers['low']) + '-' + \
                str((int(stack / stackPotScalers['low']) + 1) * stackPotScalers['low'])
    elif stack >= stackPotCutoffs['low'] and stack < stackPotCutoffs['mid']:
        rng = str(int(stack / stackPotScalers['mid']) * stackPotScalers['mid']) + '-' + \
                str((int(stack / stackPotScalers['mid']) + 1) * stackPotScalers['mid'])
    elif stack >= stackPotCutoffs['mid'] and stack < stackPotCutoffs['high']:
        rng = str(int(stack / stackPotScalers['high']) * stackPotScalers['high']) + '-' + \
                str((int(stack / stackPotScalers['high']) + 1) * stackPotScalers['high'])
    else:
        rng = str(stackPotCutoffs['high']) + '+'
    
    return rng

def range_pot(pot, small_blind_amount):
    '''create ranges from spot'''

    pot = pot / small_blind_amount
    if pot < stackPotCutoffs['low']:
        rng = str(int(pot / stackPotScalers['low']) * stackPotScalers['low']) + '-' + \
                str((int(pot / stackPotScalers['low']) + 1) * stackPotScalers['low'])
    elif pot >= stackPotCutoffs['low'] and pot < stackPotCutoffs['mid']:
        rng = str(int(pot / stackPotScalers['mid']) * stackPotScalers['mid']) + '-' + \
                str((int(pot / stackPotScalers['mid']) + 1) * stackPotScalers['mid'])
    elif pot >= stackPotCutoffs['mid'] and pot < stackPotCutoffs['high']:
        rng = str(int(pot / stackPotScalers['high']) * stackPotScalers['high']) + '-' + \
                str((int(pot / stackPotScalers['high']) + 1) * stackPotScalers['high'])
    else:
        rng = str(stackPotCutoffs['high']) + '+'
    
    return rng

def range_potrate(amount, pot, action):
    '''create ranges from action amount'''

    if pot != 0:
        rate = amount / pot

    if action in ['FOLD', 'SMALLBLIND', 'BIGBLIND']:
        rng = '-1'
    elif action in ['CALL', 'RAISE'] and rate < potRateCutoffs['low']:
        rng = str(round(int(rate / potRateScalers['low']) * potRateScalers['low'], 1)) + '-' + \
                str(round((int(rate / potRateScalers['low']) + 1) * potRateScalers['low'], 1))
    elif action in ['CALL', 'RAISE'] and rate >= potRateCutoffs['low'] and rate < potRateCutoffs['mid']:
        rng = str(round(int(rate / potRateScalers['mid']) * potRateScalers['mid'], 1)) + '-' + \
                str(round((int(rate / potRateScalers['mid']) + 1) * potRateScalers['mid'], 1))
    else:
        rng = str(potRateCutoffs['mid']) + '+'
    
    return rng
