from mpyc.runtime import mpc
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import patient

def predict_proba(X_val, coeffs):
    return 1/(1 + np.exp(-(np.dot(X_val, coeffs[1:])+coeffs[0])))

def test(patient):
    patient_array = np.array(patient.to_array())
    coeffs = np.loadtxt("../../data/trained_model_coeffs.txt")
    print("Proba for given patient using given function: {:.2f}%".format(100*predict_proba(patient_array, coeffs)))

# The function that will be given to all parties
@mpc.coroutine
async def prediction(table_shares):
    coeffs = np.loadtxt("../../data/trained_model_coeffs.txt")
    # We tried to match the given function but we had an issue using the np.exp()
    # function. Because we did not find any way to approximate the exponential function
    # using the SMC model, our prediction will not be as accurate as they are in the model.
    return 1 / (1 + -(np.dot(table_shares, coeffs[1:]) + coeffs[0]))

def main(patient):
    secfloat = mpc.SecFlt()

    #Waits and initialize all connections between parties
    mpc.run(mpc.start())

    patient_array = patient.to_array()
    share_array = []

    for i in range(len(patient_array)):
        #Secret-Shares it with all the parties
        data_share = mpc.input(secfloat(patient_array[i]), senders=0)
        share_array.append(data_share)
    
    #Start the computing process by launching all parties
    result = mpc.run(mpc.output(
        prediction(share_array)
    ))

    print("Proba for given patient using SMC: {:.2f}%".format(100 * result))

    # Disconnects every connected parties
    mpc.run(mpc.shutdown())

#-------------------------------------------------

if __name__ == '__main__':
    #Instanciate a patient, prompt the user to fill all the input data
    patient = patient.Patient()

    #Compute the prediction using the given formula
    test(patient)

    #Compute the prediction using SMC model
    main(patient)
