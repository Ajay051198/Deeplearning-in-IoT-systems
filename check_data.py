import numpy as np
file_name = "milan"
path = f"./PP_Data/{file_name}"

X = np.load(f"{path}_X.npy", allow_pickle=True)
Y = np.load(f"{path}_Y.npy", allow_pickle=True)
enc_dec = np.load(f"{path}_ENCDEC.npy", allow_pickle=True)
series = np.load(f"{path}_series.npy", allow_pickle=True)

(idx2act, idx2obs, act2idx, obs2idx) = enc_dec


#Test1

# idx = int(input('Enter index: '))
# print('-'*88)
# print(f"X-> {X[idx]}, tot: {len(X[idx])}")
# print(f"Y-> {Y[idx]}")
# print(act2idx)

#Test2
# print(len(series))
# print(series[:50])

#Test 3
print(idx2act)
print()
print("ENCODING DIM >> ")
print(len(set(obs2idx.values())))