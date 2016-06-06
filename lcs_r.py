""" Longest common subsequence using recursion , this is test
"""

def lcs_r(x,y,m,n):
    if m==0 or n ==0 :
        return 0
    if x[m-1] == y[n-1]:
        return (1+lcs_r(x[:m-1],y[:n-1],m-1,n-1))
    else:
        return max(lcs_r(x[:m-1],y[:n],m-1,n),lcs_r(x[:m],y[:n-1],m,n-1))

if __name__ == '__main__':
    x = input()
    m = len(x)
    y = input()
    n = len(y)
    #print (x[m-1]+' , '+y[n-1])
    print (lcs_r(x,y,m,n))
