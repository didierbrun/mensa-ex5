input = ['100 7 8',
'2 6 4 0 7 8 8 8 1 0 3 2 0 0 3 3 6 3 5 1 3 8 5 1 1 6 3 3 8 2 5 4 9 8 5 7 5 0 5 3 8 7 6 0 9 7 3 8 4 4 5 7 6 0 8 7 6 4 5 4 6 3 3 2 0 7 9 9 6 5 9 1 0 8 1 2 1 7 8 8 0 6 9 5 1 2 2 4 8 8 4 7 4 0 0 7 0 8 4 4']

n, a, c = map(int, input[0].split())
ls = list(map(int, input[1].split()))

dp = [0 for i in range(n+a+c+1)]

absorb = sum(ls[:a]) 
for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    dp[i+a+c] = max(dp[i+a+c+1], dp[i] + absorb)
    absorb += ls[i+a] if i+a < len(ls) else 0
    absorb -= ls[i]

print('Solution attendue : ', 198)
print('Solution trouvée : ', sum(ls) - max(dp))