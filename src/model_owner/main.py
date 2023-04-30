import time
from mpyc.runtime import mpc


def prediction(a, b, c):
    #Read poids.txt....
    return a + 1


# 1 Récupérer les data du client
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

secint_a = mpc.SecInt(16)(a)

secint_b = mpc.SecInt(16)(b)

secint_c = mpc.SecInt(16)(c)

mpc.run(mpc.start())

a2 = mpc.input(secint_a)
b2 = mpc.input(secint_b)
c2 = mpc.input(secint_c)

mpc.run(prediction(secint_a, secint_b, secint_b))

# print(prediction(mpc.output(mpc.sum(a2)),
#                  mpc.output(mpc.sum(b2)),
#                  mpc.output(mpc.sum(c2))))
# mpc.run(mpc.output(mpc.sum(a)))


# print("Hello world from Model Owner !")

# print(''.join(mpc.run(mpc.transfer("Hello world !"))))

# get l'input
#call prediction ?

# mpc.run(mpc.output(42))
mpc.run(mpc.shutdown())
