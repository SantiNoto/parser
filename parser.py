import re
file = open("Documents/GitHub/parser/match_complete.test")
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
                continue
            if "mobidb-lite" in tag:
                movidb=True
                continue
            if "lcn" in tag and movidb:
                elements = tag.split('"')
                start=elements[1]
                end=elements[3]
                print(proteinID+":"+start+"-"+end)
                
                movidb=False
file.close()
