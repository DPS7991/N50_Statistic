import sys

fasta_file = str(sys.argv[1])

def parse_fasta(fname):
    with open(fname, "r") as fh:
        identifier = None
        sequence = []

        for line in fh:
            line = line.strip() 
            if line.startswith(">"):
                if identifier:
                    yield (identifier, ''.join(sequence))
                    identifier = line
                    sequence = []
                else:
                    identifier = line
                    sequence = []
            else:
                sequence.append(line)
        
        if identifier:
            yield (identifier, ''.join(sequence))

list_of_lengths = []
    
for identifier, sequence in parse_fasta(fasta_file):
    sequence_length = len(sequence)
    list_of_lengths.append(sequence_length)

def calc_N50(list_of_lengths):
	sorted_list = sorted(list_of_lengths, reverse=True)
	total = sum(sorted_list)
	half_total = int(total / 2)

	sum_total = 0
	new_sorted_list = []

	for length in sorted_list:	
		sum_total += length
		new_sorted_list.append(length)

		if sum_total >= half_total:
			break
	
	return new_sorted_list[-1]

print(f'The N50 statistic is {int(calc_N50(list_of_lengths))}')
