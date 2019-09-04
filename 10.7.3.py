# Chapter 10 Section 8 Exercise 3


def cumu_sum(t, jes= None):
    """ Returns a cumulative sum list using a provided
        list and an algorithm that uses of recursion  """

    assert isinstance(t, list)
    if jes is None: jes = list()
    le = len(t)
    
    if le is 1:
        jes.extend(t)
        return sorted(jes)
    else:
        jes.append(sum(t))
        t = t[:le - 1]
        return cumu_sum(t, jes)

if __name__ == '__main__':
    
    list1 = [1,5,6,11,7,2,3,9]
    list2 = [1,6,12,23,30,32,35,44]
    list3 = cumu_sum(list1)

    list4 = [1,5,2,3]
    list5 = [1,6,8,11]
    list6 = cumu_sum(list4)

    print list3 == list2, list6 == list5

    print list3, list6



