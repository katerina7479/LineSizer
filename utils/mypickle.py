import cPickle as pickle
from sqlite3 import Binary


def un_pickle(mybinary):
    data = pickle.loads(str(mybinary))
    return data


def get_pickle(data):
    mypickle = pickle.dumps(data, protocol=2)
    mybinary = Binary(mypickle)
    return mybinary
