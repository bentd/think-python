# Chapter 10 Section 7 Exercise 2

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    res = []
    for s in t:
        if isinstance(s, list): res.append(capitalize_nested(s))
        elif isinstance(s, str): res.append(s.capitalize())
        else: continue
    return res

def capitalize_list(t):
    " old "
    res = []
    for i in t:
        if type(i) is str: res.append(i.capitalize())
        else: res.append(i)
    return res

def capitalize_nested_list(t):
    " old "
    nes = []
    for s in t:
        if type(s) is list: nes.append(capitalize_list(s))
        elif type(s) is str: nes.append(s.capitalize())
        else: nes.append(s)
    return nes



if __name__ == '__main__':

    list1 = ['a','p','p','l','e',2]

    list2 = capitalize_list(list1)

    list3 = [list1, list2, ['p','i','n','e','a','p','p','l','e']]
    
    list4 = capitalize_nested_list(list3)

    print list1, list2, list3, list4


