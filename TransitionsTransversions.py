__author__ = 'Kurt Graff'

def problem(s1, s2):
    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    ratio = {True: 0.0, False: 0.0}
    for p in zip(s1, s2):
        if p[0] != p[1]:
            ratio[p in transitions] += 1
    return ratio[True] / ratio[False]
def parse_fasta(file):
    data = open(file).readlines()
    records = {}
    record_id = 0
    for line in data:

        if line.startswith('>'):
            record_id = line[1:].rstrip()

            records[record_id] = ''
        else:


            records[record_id] += line.rstrip()
    return records



test = parse_fasta('rosalind_tran.txt')
key,s2 = test.popitem()
key,s1 = test.popitem()

print(problem(s1, s2))