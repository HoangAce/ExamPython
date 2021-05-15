# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 0
while nterms <= 0:
# check if the number of terms is valid
   print("Plese enter a positive integer")
   nterms  = int(input())
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i), end = " ")
