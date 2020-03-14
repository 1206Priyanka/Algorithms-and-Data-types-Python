



def linear_search(A,x):
    answer =-1
    for i in range (0,len(A)):
        if A[i]==x: answer = i
        print(answer)
linear_search ([10,5,9,9],10)



print("\n")

def better_linear_search(A,x):
    for i in range(0,len(A)):
        if A[i]==x: return i
        print(i)
    

better_linear_search ([10,5,9,9],10)
