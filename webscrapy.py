import urllib2

"""
Dictionary containing the State and UT codes
as keys and the number of constituencies as values
"""
entities_dict = {"U01": 1,
                 "S01": 42,
                 "S02": 2,
                 "S03": 14,
                 "S04": 40,
                 "U02": 1,
                 "S26": 11,
                 "U03": 1,
                 "U04": 1,
                 "S05": 2,
                 "S06": 26,
                 "S07": 10,
                 "S08": 4,
                 "S09": 6,
                 "S27": 14,
                 "S10": 28,
                 "S11": 20,
                 "U06": 1,
                 "S12": 29,
                 "S13": 48,
                 "S14": 2,
                 "S15": 2,
                 "S16": 1,
                 "S17": 1,
                 "U05": 7,
                 "S18": 21,
                 "U07": 1,
                 "S19": 13,
                 "S20": 25,
                 "S21": 1,
                 "S22": 39,
                 "S23": 2,
                 "S24": 80,
                 "S28": 5,
                 "S25": 42}

for item in entities_dict.keys():
    ctr = int(entities_dict[item])
    for i in range(ctr + 1)[1:]:
        filename = "Constituencywise" + item + str(i) + ".htm"
        try:
            data = urllib2.urlopen('http://eciresults.nic.in/%s?ac=%d'
                                   % (filename, i))
            with open('%s' % (filename), "w") as f:
                temp = data.read()
                f.write(temp)
        except Exception as e:
            print "Exception occured:", e
            print "Filename:", filename
            pass
