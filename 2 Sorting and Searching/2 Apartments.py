'''

CSES - Apartments



Time limit: 1.00 s
Memory limit: 512 MB

There are n applicants and m free apartments. Your task is to distribute the apartments so that as many applicants as possible will get an apartment.


Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.

Input


The first input line has three integers n, m, and k: the number of applicants, the number of apartments, and the maximum allowed difference.


The next line contains n integers a_1, a_2, ..., a_n: the desired apartment size of each applicant. If the desired size of an applicant is x, he or she will accept any apartment whose size is between x-k and x+k.


The last line contains m integers b_1, b_2, ..., b_m: the size of each apartment.

Output


Print one integer: the number of applicants who will get an apartment.

Constraints

 1 <= n, m <= 2 * 10^5
 0 <= k <= 10^9
 1 <= a_i, b_i <= 10^9

Example


Input:
4 3 5
60 45 80 60
30 60 75


Output:
2 
'''
def main():
    n, m, k = map(int, input().split())

    a = list(sorted(map(int, input().split())))
    b = iter(list(sorted(map(int, input().split()))))

    ans = 0
    
    b_i = next(b, None)
    
    for a_i in a:
        while 1:
            if not b_i:
                break
            if b_i < a_i and a_i - b_i > k:
                b_i = next(b, None)
                continue
            elif abs(a_i - b_i) <= k:
                b_i = next(b, None)
                ans+=1
                break
            else:
                break
    
    return ans
            
print(main())