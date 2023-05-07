from mpyc.runtime import mpc
import mpyc
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def load_dataset(file):
    data=pd.read_csv("../../data/framingham_heart_disease_test.csv")
    # X/y splitting of data
    X = data.drop('TenYearCHD',axis=1)
    y=data['TenYearCHD']
    return X, y


def predict_proba(X_val, coeffs):
    return 1/(1 + np.exp(-(np.dot(X_val, coeffs[1:])+coeffs[0])))

def test():
    X_test, y_test = load_dataset("framingham_heart_disease_test.csv")
    coeffs = np.loadtxt("../../data/trained_model_coeffs.txt")
    print("Proba for X_test[0]: {:.2f}%".format(100*predict_proba(X_test.iloc[0].to_numpy(), coeffs)))
    print("Proba for X_test[29]: {:.2f}%".format(100*predict_proba(X_test.iloc[29].to_numpy(), coeffs)))

#--------------------------------------------------------

@mpc.coroutine
async def prediction(male_share, age_share,
                     currentSmoker_share, cigsPerDay_share,
                     BPMeds_share, prevalentStroke_share, prevalentHyp_share,
                     diabetes_share, totChol_share, sysBP_share, diaBP_share,
                     BMI_share, heartRate_share, glucose_share):
    coeffs = np.loadtxt("../../data/trained_model_coeffs.txt")
    table_share = [male_share, age_share,currentSmoker_share,
                   cigsPerDay_share,BPMeds_share, prevalentStroke_share,
                   prevalentHyp_share, diabetes_share,totChol_share,
                   sysBP_share, diaBP_share, BMI_share,heartRate_share, glucose_share]
    #TODO Add exp here
    return 1 / (1 + -np.dot(table_share, coeffs[1:]) + coeffs[0])

def main():

    secint = mpc.SecInt()
    secfloat = mpc.SecFlt()

    mpc.run(mpc.start())
    print(mpc.parties)

    # Values here from input party
    male = 1
    age = 53
    currrentSmoker = 0
    cigsPerDay = 0
    BPMeds = 0
    prevalentStroke = 0
    prevalentHyp = 0
    diabetes = 220.0
    totChol = 127.0
    sysBP = 76.0
    diaBP = 24.27
    BMI = 75.0
    heartRate = 74.0
    glucose = 0.0

    #Secret-Shares it with all the parties
    male_share = mpc.input(secfloat(male), senders=0)
    age_share = mpc.input(secfloat(age), senders=0)
    currentSmoker_share = mpc.input(secfloat(currrentSmoker), senders=0)
    cigsPerDay_share = mpc.input(secfloat(cigsPerDay), senders=0)
    BPMeds_share = mpc.input(secfloat(BPMeds), senders=0)
    prevalentStroke_share = mpc.input(secfloat(prevalentStroke), senders=0)
    prevalentHyp_share = mpc.input(secfloat(prevalentHyp), senders=0)
    diabetes_share = mpc.input(secfloat(diabetes), senders=0)
    totChol_share = mpc.input(secfloat(totChol), senders=0)
    sysBP_share = mpc.input(secfloat(sysBP), senders=0)
    diaBP_share = mpc.input(secfloat(diaBP), senders=0)
    BMI_share = mpc.input(secfloat(BMI), senders=0)
    heartRate_share = mpc.input(secfloat(heartRate), senders=0)
    glucose_share = mpc.input(secfloat(glucose), senders=0)
    

    # result = mpc.run(mpc.output(result_share))
    result = mpc.run(mpc.output(
        prediction(male_share, age_share, currentSmoker_share,
                   cigsPerDay_share, BPMeds_share, prevalentStroke_share,
                   prevalentHyp_share, diabetes_share, totChol_share,
                   sysBP_share, diaBP_share, BMI_share, heartRate_share,
                   glucose_share)
    ))

    print("Proba for current patient: {:.2f}%".format(100 * result))

    mpc.run(mpc.shutdown())

if __name__ == '__main__':
    #test()
    main()
#------------------------------------------------------------

# s = mpc.input(secret_number, senders=0)
# test = mpc.run(prediction(secret_number))

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
