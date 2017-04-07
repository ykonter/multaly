from firebase import firebase
from datetime import datetime


def data_gen():
    t_stamp = datetime.now()
    data = {'time_stamp': t_stamp, 'year': t_stamp.year,
            'month': t_stamp.month, 'day': t_stamp.day}
    return data


def prompt_create_new_tally(tally_name):

    assert isinstance(tally_name, str)
    print("'{}' has not been found in your library.\nWould you like to add it [y/n]?".format(tally_name))

    answer = input()
    for i in range(5):
        if answer == '':
            answer = input('[y/n] :: ')

    if answer.lower() == 'y':
        return True

    return False


def push(record, root=''):

    # check validity of input
    assert isinstance(record, str)

    # setup values
    record = record.lower().strip()
    data = data_gen()

    # create instance
    fb = firebase.FirebaseApplication('https://multally.firebaseio.com/')

    # fetch available categories
    result = fb.get(root, '')
    assert isinstance(result, dict)
    keys = [x for x in result]

    # unknown option handler
    if record not in keys:
        if not prompt_create_new_tally(record):
            print('record not submitted')
            return

    # submit record
    fb.post('{}/{}'.format(root, record), data=data)





