import sys

LINE_DELIMITER = '|'
VALUE_DELIMITER = ':'

if(len(sys.argv) < 2):
    sys.exit("There must be one argument: a filename or filepath")
fileinput = sys.argv[1]

total = 0
number_of_entries = 0
with open(fileinput, 'r', 0) as data_file:
	for line in data_file:
		value = line.strip().split(LINE_DELIMITER)[-1].strip().split(VALUE_DELIMITER)[-1].strip()
		total += float(value)
		number_of_entries += 1

print 'Mean: {}'.format(total/number_of_entries)