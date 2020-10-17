import numpy as np
file_name = input("enter file name: ")
path = f"./PP_Data/{file_name}"

single = int(input('Binary Task (1/0): '))

if single:
    X = np.load(f"{path}_X_Single.npy", allow_pickle=True)
    Y = np.load(f"{path}_Y_Single.npy", allow_pickle=True)
    enc_dec = np.load(f"{path}_ENCDEC_Single.npy", allow_pickle=True)
else:
    X = np.load(f"{path}_X.npy", allow_pickle=True)
    Y = np.load(f"{path}_Y.npy", allow_pickle=True)
    enc_dec = np.load(f"{path}_ENCDEC.npy", allow_pickle=True)

(idx2act, idx2obs, act2idx, obs2idx) = enc_dec


# Test1
# idx = int(input('Enter index: '))
# print('-'*88)
# print(f"X-> {X[idx]}, tot: {len(X[idx])}")
# print(f"Y-> {Y[idx]}")
# print(act2idx)

# Test2
# print(len(series))

# Test 3
print(f"Size >> {len(X)}")
print()
print(idx2act)
print(np.unique(Y))
print()
print(f"ENCODING DIM >> {len(set(obs2idx.values()))}")
