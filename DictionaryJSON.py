
"""
Created by Sarmad Syed 11/1/2016
"""
"""
Takes in two JSON files, and compares
the values and outputs a list showing
the differences
actual = {
    'FirstName' : 'Joe',
    'BankInfo' : { 'bankName' : 'BOA',
                    'accountNumber' : 123
                  }
}

expected = {
    'FirstName' : 'Joe'
    'Last Name' : 'Shmoe',
    'BankInfo' : { 'bankName' : 'BOA',
                   'checking bal' : 500
                 }
}

output = [
        ['-', 'Last Name', 'Schmoe' ],
        ['-', 'BankInfo.checking bal', 500],
        ['+', 'FirstName', 'Joe'],
        ['+', 'BankInfo.accountNumber, 123]
]
"""
def compareJSON(actual, expected):
    """Compares Two JSON Strings actual and expected and returns a list of missing values"""
    if len(actual) == 0 or len(expected) == 0:
        return []
    res = []
    actual_flat = flatten_dict(actual)
    expected_flat = flatten_dict(expected)
    for k, v in zip(actual_flat.keys(), expected_flat.keys()):
        if v not in actual_flat.keys():
            res.append(['-', v, expected_flat.get(v)])
        if k in expected_flat.keys():
            res.append(['+', k, actual_flat.get(k)])

    return res


def flatten_dict(d):
    def items():
        for k, v in d.items():
            if isinstance(v, dict):
                for s_k, s_v in flatten_dict(v).items():
                    yield k + "." + s_k, s_v
            else:
                yield k, v
    return dict(items())
    pass



def unflatten_dict(d):
    result_dict = {}
    for k, v in d.items():
        if isinstance(k, str) and '.' in k:
            parts = k.split('.')
            d = result_dict
            for p in parts[:-1]:
                if p not in d:
                    d[p] = dict()
                d = d[p]
            d[parts[-1]] = v
        else:
            result_dict[k] = v
    return result_dict


print unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c.x.z':4, 'c.y': 4, 1: 'x', 'd.x.y.z.t' : 5})

def test1():
    a = {
     'apples': 1,
     'oranges': 2
    }

    b = {
        'apples': 1,
        'grapes': 2
    }

    return compareJSON(a, b)

def test2():

    a = {
        'apples' : 1,
        'oranges' : {
            'navel' : 1,
            'Florida' : 'Yes'
        }
    }

    b = {
        'apples' : 1,
        'oranges' : {
            'California' : 'Yes',
            'navel' : 1
        }
    }
    return compareJSON(a, b)

def test3():

    a = {
        'apples' : 1,
        'oranges' : {
            'navel' : 1,
            'Florida' : 'Yes'
        },
        'bud' : {
            'Strain' : 'OG',
            'Leafy' : 'Yes',
            'Type' : {
                'indica' : 'Yes'
            }
        }
    }

    b = {
        'apples' : 1,
        'oranges' : {
            'California' : 'Yes',
            'navel' : 1
        },
        'bud' : {
            'Strain' : 'OG',
            'Type' : { 'indica' : 'yes',
                       'Sativa' : 'No'
                     }
        }
    }
    return compareJSON(a, b)

#print test1()
#print test2()
#print test3()
