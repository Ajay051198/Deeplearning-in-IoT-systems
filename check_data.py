import numpy as np
file_name = "cairo"
path = f"./PP_Data/{file_name}"

X = np.load(f"{path}_X.npy", allow_pickle=True)
Y = np.load(f"{path}_Y.npy", allow_pickle=True)
enc_dec = np.load(f"{path}_ENCDEC.npy", allow_pickle=True)

(idx2act, idx2obs, act2idx, obs2idx) = enc_dec

idx = int(input('Enter index: '))
print('-'*88)
print(f"X-> {X[idx]}, tot: {len(X[idx])}")
print(f"Y-> {Y[idx]}")
print(act2idx)