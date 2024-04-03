import argparse

def searchandoutput(inputfile, outputfile, match_string):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    matching_lines = [line for line in lines if match_string in line]

    with open(output_file, 'w') as f_out:
        f_out.writelines(matching_lines)

if __name == "__main":
    parser = argparse.ArgumentParser(description="Match string in input file and output lines containing the string to another file")
    parser.add_argument("-i", "--input", help="Input file path", required=True)
    parser.add_argument("-o", "--output", help="Output file path", required=True)
    parser.add_argument("-m", "--match", help="String to match", required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    match_string = args.match

    search_and_output(input_file, output_file, match_string)
