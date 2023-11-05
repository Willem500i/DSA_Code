def appearances(s, low, high):
    if len(s) == 0:
        return {}
    elif low == high:
        return {s[low]:1}
    else:
        dic = appearances(s, low+1, high)
        if s[low] in dic:
            dic.update({s[low]: dic[s[low]] + 1})
        else:
            dic.update({s[low]:1})
        return dic