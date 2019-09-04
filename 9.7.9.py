# CarTalk Puzzle 3

def age_test(son_age, older):
    """ Tests whether sons age is reverse of mothers who is years 'older' """
    if not type(older)==str: older=str(older)
    son_age=str(son_age)
    mom_age=str(eval(son_age+'+'+older))
    if len(son_age)<2: son_age=son_age.zfill(2)
    if son_age==mom_age[::-1]: return True
    else: return False

def ages(older):
    """ Finds number of times sons age is reverse of mothers who is years 'older' """
    age_range=range(101)
    count=0
    for number in age_range:
        if age_test(number, older): count+=1
    return count

def years():
    """ Finds and uses possible age difference in which the son and mother have reversible ages 8 times
        and prints those 16 ages """
    difference_range=range(15,61)
    for difference in difference_range:
        if ages(difference)==8:
            print '\n\n','Here are the 8 times when mother and son have reversible ages: \n\n'
            for possible_sons_age in range(101):
                possible_sons_age=str(possible_sons_age)
                if age_test(possible_sons_age, difference): print possible_sons_age.zfill(2),'',eval(possible_sons_age+'+'+'difference')
        else: continue
    else: print 

years()












#Authors
# ______________________________________________________________________________


def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print daughter, mother
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print diff, n
        diff = diff + 1

print 'diff  #instances'
check_diffs()

print
print 'daughter  mother'
num_instances(18, True)

#_______________________________________________________________-

print '\n'
