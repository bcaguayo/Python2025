import pickle

with open('bin.dat', 'rb') as file:
    data = pickle.load(file)
    print(data)

# data imported if of type Dictionary