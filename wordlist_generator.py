import itertools
import optparse

def generate_wordlist(letters, min_length, max_length, filename):
    count = 0
    with open(filename, 'w') as file:
        for n in range(min_length, max_length + 1):
            for combinations in itertools.product(letters, repeat=n):
                file.write(''.join(combinations) + '\n')
                count += 1
    return count
def parameters():
    parser = optparse.OptionParser()
    parser.add_option("--c", dest="characters", help="please specify the letters that you want to create a wordlist")
    parser.add_option("--min", dest="min_length", type="int", help="minimum length that you want to create a wordlist")
    parser.add_option("--max", dest="max_length", type="int", help="maximum length that you want to create a wordlist")
    parser.add_option("--f", dest="filename", help="Specify filename where you want to store the wordlist")
    (options, args) = parser.parse_args()

    if not options.characters:
        parser.error("Please specify the characters to include in the wordlist")
    if not options.min_length:
        parser.error("Please specify the minimum length of words")
    if not options.max_length:
        parser.error("Please specify the maximum length of words")
    if not options.filename:
        parser.error("Please specify the filename to store the wordlist")

    words_count = generate_wordlist(options.characters, options.min_length, options.max_length, options.filename)
    print(f"{words_count} words are generated and stored in {options.filename}")

parameters()
