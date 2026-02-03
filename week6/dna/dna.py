import csv
import sys


def main():
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database_file = sys.argv[1]
    with open(database_file, "r") as file:
        reader = csv.DictReader(file)
        strs = reader.fieldnames[1:]  # STRs are all columns except the first ("name")
        database = [row for row in reader]  # List of dicts for each person

    # Read DNA sequence file into a variable
    dna_file = sys.argv[2]
    with open(dna_file, "r") as file:
        dna_sequence = file.read()

    # Find longest match of each STR in DNA sequence
    str_counts = {}
    for s in strs:
        str_counts[s] = longest_match(dna_sequence, s)

    # Check database for matching profiles
    for person in database:
        match = True
        for s in strs:
            if int(person[s]) != str_counts[s]:
                match = False
                break
        if match:
            print(person["name"])
            return

    # If no match found
    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    for i in range(sequence_length):
        count = 0
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()
