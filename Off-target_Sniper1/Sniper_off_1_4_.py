import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, concatenate, Dense, Dropout, Activation, Flatten, Conv1D, AveragePooling1D
import numpy as np
import pandas as pd
from sklearn import metrics
import sklearn
import math

header=['Guide (X20)','target + PAM']

dataset_ = pd.read_csv('input_example.csv',header=None,names=header)
final_model = tf.keras.models.load_model('Sniper_off_1_4_89d16238b3e8a326c2120c037d382655',compile=False)

length=20

def preprocess_mismatch(data,data1):
    print("Start preprocessing the sequence mismatch")
    global length

    DATA_X = np.zeros((len(data),length*12), dtype=int)
    print(np.shape(data), len(data), length)
    for l in range(len(data)):
        for i in range(length):
            if (data[l][i] in "Aa") and (data1[l][i+4] in"Tt"): DATA_X[l,i*12] =1
            elif (data[l][i] in "Aa") and (data1[l][i+4] in"Cc"): DATA_X[l,i*12+1] =1
            elif (data[l][i] in "Aa") and (data1[l][i+4] in"Gg"): DATA_X[l,i*12+2] =1
            elif (data[l][i] in "Tt") and (data1[l][i+4] in"Aa"): DATA_X[l,i*12+3] =1
            elif (data[l][i] in "Tt") and (data1[l][i+4] in"Cc"): DATA_X[l,i*12+4] =1
            elif (data[l][i] in "Tt") and (data1[l][i+4] in"Gg"): DATA_X[l,i*12+5] =1
            elif (data[l][i] in "Cc") and (data1[l][i+4] in"Aa"): DATA_X[l,i*12+6] =1
            elif (data[l][i] in "Cc") and (data1[l][i+4] in"Tt"): DATA_X[l,i*12+7] =1
            elif (data[l][i] in "Cc") and (data1[l][i+4] in"Gg"): DATA_X[l,i*12+8] =1
            elif (data[l][i] in "Gg") and (data1[l][i+4] in"Aa"): DATA_X[l,i*12+9] =1
            elif (data[l][i] in "Gg") and (data1[l][i+4] in"Tt"): DATA_X[l,i*12+10] =1
            elif (data[l][i] in "Gg") and (data1[l][i+4] in"Cc"): DATA_X[l,i*12+11] =1
    return DATA_X

def preprocess_seq(data,data1):
    print("Start preprocessing the sequence done 2d")
    global length

    DATA_X = np.zeros((len(data),length,8), dtype=int)
    print(np.shape(data), len(data), length)
    for l in range(len(data)):
        for i in range(length):

            try: data[l][i]
            except: print(data[l], i, length, len(data))

            if data[l][i]in "Aa":    DATA_X[l, i, 0] = 1
            elif data[l][i] in "Cc": DATA_X[l, i, 1] = 1
            elif data[l][i] in "Gg": DATA_X[l, i, 2] = 1
            elif data[l][i] in "Tt": DATA_X[l, i, 3] = 1
            elif data[l][i] in "Xx": pass
            else:
                print("Non-ATGC character " + data[l])
                print(i)
                print(data[l][i])
                sys.exit()

            if data1[l][i+4]in "Aa":    DATA_X[l, i, 4] = 1
            elif data1[l][i+4] in "Cc": DATA_X[l, i, 5] = 1
            elif data1[l][i+4] in "Gg": DATA_X[l, i, 6] = 1
            elif data1[l][i+4] in "Tt": DATA_X[l, i, 7] = 1
            elif data1[l][i+4] in "Xx": pass
            else:
                print("Non-ATGC character " + data1[l])
                print(i)
                print(data1[l][i+4])
                sys.exit()
        #loop end: i
    #loop end: l
    print("Preprocessing the sequence done")
    return DATA_X

dataset_mismatch = pd.DataFrame(preprocess_mismatch(dataset_['Guide (X20)'],dataset_['target + PAM']))

dataset_seq_masked = preprocess_seq(dataset_['Guide (X20)'],dataset_['target + PAM'])

dataset_seq_masked = pd.Series(list(dataset_seq_masked),name='seq')

dataset_all = pd.concat([dataset_,dataset_mismatch,dataset_seq_masked],axis=1)

X_test_seq = np.stack(dataset_all['seq'])
X_test_feature = np.asarray(dataset_all.iloc[:,2:-1]).astype(np.float32)
hyperparameter_prediction = final_model.predict([X_test_seq,X_test_feature], batch_size=128)
hyperparameter_prediction = pd.DataFrame(hyperparameter_prediction)

hyperparameter_prediction=pd.concat([dataset_all['Guide (X20)'].reset_index(drop=True),dataset_all['target + PAM'].reset_index(drop=True),hyperparameter_prediction.reset_index(drop=True)],axis=1,ignore_index=True)
hyperparameter_prediction.columns=['Guide (X20)','target + PAM','Prediction score']
hyperparameter_prediction.to_excel('prediction_result.xlsx' ,engine='openpyxl')
