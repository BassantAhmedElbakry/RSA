# RSA

import random
import math

def is_prime(num):
  """
  This function checks if a number is prime using trial division.
  """
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def generate_random_prime(lower, upper):
  """
  This function generates a random prime number between lower and upper (inclusive).
  """
  while True:
    # Generate a random odd number within the range
    num = random.randrange(lower, upper + 1, 2)
    if is_prime(num):
      return num
    
# p & q
p = generate_random_prime(3, 17)
q = generate_random_prime(3, 11) 
while p == q:  
  p = generate_random_prime(3, 17)
  q = generate_random_prime(3, 11) 

print("p = ", p)
print("q = ", q)

# n = p x q
n = p * q 
print("n = ", n)

# phi(n) = (p - 1) x (q - 1)
phi_n = (p - 1) * (q - 1)
print("Phi(n) = ", phi_n)

# Generate e
e = generate_random_prime(3, phi_n - 1)
# Check for relatively prime with GCD (coprime)
while math.gcd(e, phi_n) != 1:  
  e = generate_random_prime(3, phi_n - 1)
print("e = ", e)

# Generate d
found_valid_d = False
while not found_valid_d:
  i = random.randrange(1, phi_n - 1)
  d = (((i * phi_n) + 1) / e)
  # Check if d is an integer and d less than phi(n)
  if d % 1 == 0 and d < phi_n:  
    found_valid_d = True

# Print d after finding a valid integer value
print("d = ", d)
print("i = ", i)

# Counter to check that all tests Passed
counter = 0

# Generate Messages from 1 --> n as M should be < n
# (M < n)
for M in range(n): 
  
  # Ciphertext (Encryption)
  C = (M ** e) % n

  # Decryption
  Decryption_M = (C ** int(d)) % n

  ############################################ TEST ############################################
  # Run from M = 1 to M = n - 1 as Message shoud be < n  
  
  if M == Decryption_M:
    counter = counter + 1
  else:
    print("TEST ", M + 1," FAILED :( ")

 
# Check on all tests 
if counter == n:
  print("\n Congratulations !!!!!!!! \n All tests Passed :) \n")
else:
  print("Some tests Failed :(")
  

    