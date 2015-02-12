import urllib2

entities_dict = {
                    "U05": 70,
                }

for item in entities_dict.keys():
    ctr = int(entities_dict[item])
    for i in range(ctr + 1)[1:]:
        filename = "Constituencywise" + item + str(i) + ".htm"
        try:
            data = urllib2.urlopen('http://eciresults.nic.in/%s?ac=%d'
                                    % (filename, i))
            with open('data/%s' % (filename), "w") as f:
                temp = data.read()
                f.write(temp)
        except Exception as e:
            print "Exception occured:", e
            print "Filename:", filename
            pass
