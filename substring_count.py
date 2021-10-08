def count_substring(st, sub):
    a = st[:]
    pos, pos_1 = 0, 0
    cnt = -1
    end = len(st)
    while pos_1 != -1:
        pos_1 = a.find(sub, pos, end)
        pos = pos_1 + 1
        cnt +=1
    return cnt
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
