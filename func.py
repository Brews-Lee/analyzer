from pathlib import Path

# The values to search for in each line of the csv file, modify this if the format changes!!
MAILBOX = "mailBox"
BREACHDATE = "breachDate"


# Takes a path to a file or directory as input 
# Returns a list containing lists contaning a dictionary contaning the mailBox nad breachDate information
#   Each inner list is for a separate file, each inner-inner list is for a separate line
#   in the file and each dictionary within that list has a key:value pair for
#   each column in the csv file
# Ignores non-csv files and subdirectories
def get_data(path: str, separator: str) -> list:
    files = list()
    
    if path.is_dir():
        files = [str(x) for x in list(path.iterdir()) if x.suffix == ".csv"]
    else:
        files.append(str(path))
        
    info = dict()
    data = list()
    i = 0
    for file in files:
        data.append([])
        with open(file, 'r') as f:
            for row in f:
                row = row.replace('"', '')
                row = row.split(separator)
                info.clear()
                for section in row:
                    if MAILBOX in section:
                        info.update({MAILBOX: section.split(": ")[1]})
                    elif BREACHDATE in section:
                        info.update({BREACHDATE: section.split(": ")[1]})
                if bool(info):
                    data[i].append(info.copy())
            i += 1
    return data

def check_occurences(data: list):
    mails = dict()
    # Load all mails present in the files
    for file in data:
        for row in file:
            # If mail is already in dictionary, then increment
            if row[MAILBOX] in mails.keys():
                mails[row[MAILBOX]] += 1
            else:
                mails.update({row[MAILBOX]: 1})
    mails = dict(sorted(mails.items(), key=lambda item: item[1])) # sorts the dictionary by value
    print("MAIL: COUNT\n")
    for mail, count in mails.items():
        print(mail + ": " +  str(count))

# Takes the list with with data gotten with the get_data function
# Prints the results to standard output or to a file (--output)
# Returns 0 on success and 1 on error
def analyze(data: list, output: str) -> int:
    # Check for mailBox occurences over multiple file
    check_occurences(data)
