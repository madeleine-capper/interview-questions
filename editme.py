#
#
# Hi! This script is intended to add tags and edit
# any answers for the
# Data Science Interview Question Wizard.
# It loops through the master list of dictionaries saved in masterlist.pkl
# and allows for edits on an interative basis :)
# It will continuously save in a new list of dictionaries called
# templist.pkl so as not to overwrite the master.
# please replace masterlist.pkl with templist.pkl when finished
# if no corruption or errors have incurred.
# safe travels~
#
#
# set global variables
import pickle
import sys
OPTIONSDICT = {
    1: 'Data Engineering and ETL',
    2: 'Machine Learning Engineering',
    3: 'Data Science (general)',
    4: 'Programming (general)',
    5: 'Statistics',
    6: 'Problem Solving'}

OPTIONS = \
    '''
1: Data Engineering and ETL
2: Machine Learning Engineering
3: Data Science (general)
4: Programming (general)
5: Statistics
6: Problem Solving
'''
# load up the masterlist and store in memory as listodicts
with open('masterlist.pkl', 'rb') as f:
    listodicts = pickle.load(f)
# initialize response


def exitprotocol(offset=0):
    '''
    saves the templist file and exists the program.
    '''
    with open('savestate.pkl', 'wb') as f:
        pickle.dump(offset, f)
    with open('templist.pkl', 'wb') as f:
        pickle.dump(listodicts, f)
    print('bye!')
    exit(0)


def main(i=0):
    '''
    main loop will iterate over i for the list of dictionaries 
    for editing unless killed.
    '''
    if i == 0:
        response = input('''
        Welcome to the editing wizard!
        If you would like to exit at any time, 
        type 
        PERSIMMONTIME
        into the command line and 
        you will be exited from the program with a saved 'templist.pkl'.
        
        Would you like to begin the process? [y/n]
        ''')
    else:
        response = 'y'
    if response[0].lower() == 'y':
        print('Question:')
        print(listodicts[i]['question'])
        print('------')
        print('Answer:')
        print(listodicts[i]['answer'])
        print('------')
        print('current tags: ')
        print(listodicts[i]['tags'])
        print('====================\n====================')
        response = input(
            'Would you like to add a tag? [y/n]\n'
        )
        if response[0].lower() == 'y':
            topics = []
            while True:
                response = input(
                    'Please select a topic tag numeral. 0 to exit. \n'
                    + OPTIONS)
                if response.isdigit():
                    if int(response) in range(1, 7):
                        topics.append(int(response))
                        response = input(
                            'Do you want to select another topic?\n')
                        if response[0].lower() == 'y':
                            pass
                        else:
                            break
                    elif int(response) == 0:
                        print('its ok to change yr mind!')
                        break
                    else:
                        print('please select from the options presented.\n')
                        pass
                else:
                    print('please input a numerical value.\n')
                    pass
            # associate english version associated with numerical values
            topics = [OPTIONSDICT[i] for i in topics]
            # extend tag list with whatever was added
            listodicts[i]['tags'] = list(
                set(listodicts[i]['tags']).union(set(topics))
            )
            ######
        if response != 'PERSIMMONTIME':
            listodicts[i]['question'] = edit_the_thing(
                listodicts[i]['question'], mode='question', i=0)
            listodicts[i]['answer'] = edit_the_thing(
                listodicts[i]['answer'], mode='answer', i=0)
        if ((i+1) < len(listodicts)) and (response != 'PERSIMMONTIME'):
            return main(i=i+1)
        else:
            print('saving and exiting!')
            return exitprotocol(offset=i)
    else:
        return exitprotocol(offset=i)


def edit_the_thing(subject, mode='answer', i=0):
    response = input(f'Do you want to edit the {mode}?')
    if response[0].lower() == 'y':
        print(f'Current {mode}: ', subject)
        print(f'''=====
        Please input new {mode} here.  
        press control+D to finish.
        ======
        ''')
        response = sys.stdin.readlines()[0]
        if response != 'PERSIMMONTIME':
            check = input(f'''
            Here's what you submitted:
            {response}
            -------
            good with that? (y/n)''')
            if check[0].lower() == 'y':
                return response
            elif check == 'PERSIMMONTIME':
                return exitprotocol(offset=i)
            else:
                return edit_the_thing(subject, mode=mode)
    elif response == 'PERSIMMONTIME':
        return exitprotocol(offset=i)
    else:
        return subject


if __name__ == '__main__':
    main()
