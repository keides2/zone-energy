import codecs

path_r = '/Users/keisu/Documents/GitHub/zone-energy/input.txt'
path_w = '/Users/keisu/Documents/GitHub/zone-energy/output.txt'

with open(path_w, mode='w') as f_w:
    with open(path_r) as f:
            for s_line in f:
                print("Input: ", s_line)

                dec_line = codecs.decode(s_line, 'rot13')
                print("Output: ", dec_line)

                f_w.write(dec_line)
