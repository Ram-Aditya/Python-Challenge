import pickle


fp = open("Challenge5.txt", "rb")
#fp.close()

f = open("test_unix.txt", "wb")
#pick_dict = {"a":2134, "b":"1234", "c":{"d": 1, "e":2}}
#pickle.dump(pick_dict, f)

example_dict = pickle.load(fp)
print(example_dict)
fp.close()
