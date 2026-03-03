#! /usr/bin/env python3
import sys
import json
import time
#from random import randint
from datetime import datetime
from google.cloud import logging
from logEntry import txtPayload, metadata#, jsonPayload

client = logging.Client()
# docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry:
log_name =  sys.argv[1]

# sys args definitions/time intervals;
# convert sys.arg [2], [3], [4] to int:
to_int = lambda x: int(sys.argv[x])
total_mssgs = to_int(2)
mssg_gap =  float(sys.argv[3]) #to_int(3)
ingest_interrupt = to_int(4)

# log message, to diff between stream of logs:
subject = sys.argv[5]
severity = sys.argv[6]

def send_stream(metadata): # Writes log entry
    logger = client.logger(log_name)
    logger.log_text(json.dumps(metadata), severity=severity)
    #print(f"{metadata["subject"]} {metadata["entry"]}")

def fake_log_stream():
    """ stream of log entries (arg = $2) w/uniform wait time
        between one another ($3) + interrupt > 5min ($4) """
    count = 1 # first message.
    while count < total_mssgs + 1 :
        try:
            # data to write:
            meta = metadata(count, total_mssgs, subject, log_body)
            send_stream(meta)                                                                                                                 count += 1
            print(f"Successfully sent log {count}/{total_mssgs} to {log_name}.")
        except KeyboardInterrupt:                                                                                                             print("\nLogging stopped by user.")
            meta["content"] = "Logging stream was manually stopped"
            send_stream(meta)
            break
        except Exception as e:
            #TODO re-euthentication handling
            print(f"Error occurred: {e}")
            break

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

fake_log_stream()

#TODO:
# Ctrl+C stop must generate a log
# informing server about user-triggered stop.
#
# timestamp to reflect local time
#
# argparse
#
# open multiple writing threads from the same terminal.
#
# expand on gap_between messages and interrupts: timer, number of interrupts.
#time.sleep(mssg_gap)
