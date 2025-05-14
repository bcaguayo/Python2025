import pickle

phonebook = {
    'alice' : '1',
    'bob' : '2',
    'carlos' : '3'
}

with open('bin.dat', 'wb') as file:
    pickle.dump(phonebook, file)

