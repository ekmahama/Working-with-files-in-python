import pickle
class Person:
    age = 45
    name = 'Edward Mahama'
    kis = ['Eliana', 'Edision']
    employers = {'Huawei': 2022, 'Microsoft': 2018}
    shoe_size = (42,43)



def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f'Serialized object: \n{pickled}\n')
    return pickled


def deserialized(obj):
    unpickled = pickle.loads(obj)
    print(f'Deserialized: \n {unpickled}\n')
    return unpickled


def obj_to_file(fn, obj):
    with open(fn, 'wb') as pf:
        pickle.dump(obj, pf, protocol=pickle.HIGHEST_PROTOCOL)
        return obj

def file_to_obj(fn, obj):
    with open(fn, 'rb') as pf:
        obj = pickle.load(pf)
        print(obj)
        return obj
    

# pickled = serialize(Person())
# deserialized(pickled)


obj = obj_to_file('./files_to_read/person.xzy', Person())
person = file_to_obj('./files_to_read/person.xzy', obj)
print(person.employers)