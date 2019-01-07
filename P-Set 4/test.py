import string
import math
cipher_dict = {}
shift = 5
alphalower = list(string.ascii_lowercase)
alphalower1 = list.copy(alphalower)
print(alphalower)
for i in range(len(alphalower)):
    alphalower[i] = alphalower1[i - shift]
alphaupper = list(string.ascii_uppercase)
alphaupper1 = list.copy(alphaupper)
print(alphalower)
for i in range(len(alphalower)):
    alphaupper[i] = alphaupper1[i - shift]
for i in alphalower1:
    cipher_dict[i] = alphalower[alphalower1.index(i)]
for j in alphaupper1:
    cipher_dict[j] = alphaupper[alphaupper1.index(j)]
print(cipher_dict)