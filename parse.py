import glob
import json

consolidated_list = []

for item in glob.glob('data/*.htm'):
    temp = ""
    temp_lst = []
    try:
        with open(item, 'rU') as f:
            temp = f.readlines()[1145]

            temp_dict = {}

            data_str = [x.split('>')[-1] for x in temp.split('<')][3:-11]

            temp_dict['State'] = data_str[0].split('-')[0].strip()
            temp_dict['Constituency'] = data_str[0].split('-')[-1].strip()

            # Start Index
            si = 16
            ei = (len(data_str) if len(data_str) else 0)
            temp_dict['Candidates'] = []
            while si < ei:
                candidate_dict = {}
                candidate_dict['Candidate'] = data_str[si].strip()
                candidate_dict['Party'] = data_str[si+2].strip()
                candidate_dict['Votes'] = data_str[si+4].strip()
                temp_dict['Candidates'].append(candidate_dict)
                si = si + 8

            temp_lst.append(temp_dict)

    except Exception as e:
        print "Exception:", e

    consolidated_list.append(temp_lst)

with open('data.json', 'wb') as fp:
    json.dump(consolidated_list, fp, indent=4, sort_keys=True)
