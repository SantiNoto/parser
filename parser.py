import re
file = open("/home/paccanaro/Common/PROJECTS/ConSAT/data/2018/testRun/data/match_complete.xml")
output = open("/home/paccanaro/Common/PROJECTS/ConSAT/data/2019/mobidb.prot","w")
pattern = re.compile(r'<[^>]*>')
attr = re.compile(r'\w+=\"[^"]+\"')
movidb=False
for line in file:
    for result in re.finditer(pattern, line):
        tag= result.group().strip()
        if tag[0] == '<' and tag[1] != '/' and tag.endswith(">"):
            if "protein" in tag:
                elements = tag.split('"')
                proteinID = elements[1]
            if "mobidb-lite" in tag:
                movidb=True
                continue
            if "lcn" in tag and movidb:
                elements = tag.split('"')
                start=elements[1]
                end=elements[3]
                output.write(proteinID+":"+start+"-"+end+"\n")
                #print(proteinID+":"+start+"-"+end)
                
                movidb=False
file.close()
output.close()
