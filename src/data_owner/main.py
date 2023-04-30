import time
import json
from mpyc.runtime import mpc

async def prediction(a):
    #Read poids.txt....
    return a + 1


mpc.run(mpc.start())
print(mpc.parties)
print(mpc.parties[0])

my_age = int(input("Enter age:"))

secint = mpc.SecInt(16)
secret_number = secint(my_age)

s = mpc.input(secret_number, senders=0)
test = mpc.run(prediction(secret_number))


# b = mpc.run(mpc.sum(s))
# out = mpc.run(mpc.output(b))

print(mpc.run(mpc.output(test)))

# mpc.run(mpc.output(prediction(my_age)))

# mpc.run(mpc.transfer(mpc.parties[0], my_age))

# a = 0
# receive_value = await parties[1].receive(a)

# print(receive_value)



# Découpe du secret et l'envoie à toute les autres
# parties
# our_age = mpc.input(secint(my_age))
# Calcul sur les computing parties


# Print du résultat
# print(mpc.run(mpc.output(mpc.sum(our_age))))
# print(mpc.run(mpc.output(mpc.max(our_age))))




# mpc.input(mpc.SecInt())

# print(''.join(mpc.run(mpc.transfer("Hello world !"))))
mpc.run(mpc.shutdown())


# print("Hello world from Data Owner !")


# SecInt
# mpc.input()
# mpc.output()
# mpc.sum()
#
# mpc.parties (nbr de parties connectés)
#
# print("Variable:", await mpc.output(test))
