blast = open("Documents/GitHub/parser/uniq.ids")
mobidb = open("Documents/GitHub/parser/mobidb.prot")
prot = dict()
coverage = dict()
totalProt = 0
for line in blast:
    protId,ranges = line.strip().split(':')
    start,end=ranges.split('-')
    start=int(start)
    end=int(end)
    if protId in prot.keys():
        lists=prot[protId]
        lists.append((start,end))
        prot[protId]=lists
    else:
        prot[protId]=[(start,end)]
    coverage[protId+":"+ranges]=False
    totalProt = totalProt + 1

for line in mobidb:
    protId,ranges = line.strip().split(':')
    mobiStart,mobiEnd=ranges.split('-')
    mobiStart=int(mobiStart)
    mobiEnd=int(mobiEnd)
    if protId in prot.keys():
        for residues in prot[protId]:
            start,end=residues
            if (mobiStart <= start and mobiEnd >= start) or (mobiStart <=end and mobiEnd >= end):
                coverage[protId+":"+str(start)+"-"+str(end)]=True
                

coverageCount = 0
for keys in coverage:
    if coverage[keys]:
        coverageCount = coverageCount + 1
        
print("total count after blast: " + str(totalProt))
print("covered by mobidb: " + str(coverageCount))
print("total percentage: " +str(100*coverageCount/totalProt))