#! /usr/bin/python3

""" quick, on-the-fly single log generator;
run it from the bash shell, include two args:
argv[1] is the name of the log;
argv[2] is the sequence number of to generate.
argv[3] is the text/log data."""

from sys import argv
#from google.cloud import logging
# logging_client = logging.Client()
#log_name = "my-log"
#logger = logging_client.logger(log_name)
#logger.log_text(text)
#print("Logged: {}".format(text))
#logging.Client().logger(f"{argv[1]}-{argv[2]}").log_text(argv[3])

def save_sequence(seq_file):
    """ reads sequence from file, fetches sequence#
        then it writes sequence+1 to file. """

    sequence = None
    with open(seq_file, "r+", encoding="utf-8") as file:
        sequence = int(file.read().strip())
        file.seek(0)
        file.truncate()
        print(f"Old sequence is {sequence}")
        new_sequence = sequence + 1
        print(f"New sequence: {new_sequence}.")
        file.write(str(new_sequence) + "\n")
        #file.close()

save_sequence(argv[1])

#with open("this.example", "w", encoding="utf-8") as file:
#    sequence = file.readline()
#    print(sequence.strip())
