# clean file up - remove duplicates

infilename = 'movie_lines-alphabetised-in.txt'
outfilename = 'movie_lines-alphabetised-out.txt'

lines_seen = set() # holds lines already seen
outfile = open(outfilename, "w")
for line in open(infilename, "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
