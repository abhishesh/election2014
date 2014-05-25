import glob
import json
import pprint


consolidated_list = []
"""
Read all htm files downloaded from election comission wesbite.
Parse the details of winner from each seat.
"""
for item in glob.glob('./*.htm'):
    temp = ""
    temp_dict = {}
    try:
        with open(item, 'rU') as f:
            temp = f.readlines()[1145]
            temp1 = temp.split('<')[3].split('>')[-1]
            temp_dict['State'] = temp1.split('-')[0].strip()
            temp_dict['Constitunecy'] = temp1.split('-')[-1].strip()

            temp2 = temp.split('<')[19].split('>')[-1]
            temp_dict['Candidate'] = temp2

            temp3 = temp.split('<')[21].split('>')[-1]
            temp_dict['Party'] = temp3

            temp4 = temp.split('<')[23].split('>')[-1]
            temp_dict['Votes'] = int(temp4)

    except Exception as e:
        print "Exception:", e

    consolidated_list.append(temp_dict)


"""
Dump the data in json file
"""
with open('data.json', 'wb') as fp:
    json.dump(consolidated_list, fp)
