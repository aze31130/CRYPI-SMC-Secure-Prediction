from mpyc.runtime import mpc
import mpyc

@mpc.coroutine
async def prediction(x_share: mpyc.sectypes.SecInt, y_share: mpyc.sectypes.SecInt):
    return x_share + y_share * 10


secint = mpc.SecInt()

mpc.run(mpc.start())
print(mpc.parties)


x_share = mpc.input(secint(4), senders=0)
y_share = mpc.input(secint(3), senders=0)

# result_share = x_share + y_share

# result = mpc.run(mpc.output(result_share))
result = mpc.run(mpc.output(prediction(x_share, y_share)))

print(result)

mpc.run(mpc.shutdown())

#------------------------------------------------------------

# s = mpc.input(secret_number, senders=0)
# test = mpc.run(prediction(secret_number))

# b = mpc.run(mpc.sum(s))
# out = mpc.run(mpc.output(b))

# print(mpc.run(mpc.output(test)))

# mpc.run(mpc.output(prediction(my_age)))

# mpc.run(mpc.transfer(mpc.parties[0], my_age))

# Print du résultat
# print(mpc.run(mpc.output(mpc.sum(our_age))))
# print(mpc.run(mpc.output(mpc.max(our_age))))

# print(''.join(mpc.run(mpc.transfer("Hello world !"))))


# SecInt
# mpc.input()
# mpc.output()
# mpc.sum()
#
# mpc.parties (nbr de parties connectés)
#
# print("Variable:", await mpc.output(test))
