#!/usr/bin/env python3
import json
# sound representation of a single log entry per 
# docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry
type Filename = str

def mssg_body(file):
    with open(file, "r") as f:
        body = f.read()
        return body
      
def metadata(count: int,
             total_mssgs: int,
             #timestamp: datetime,
             str_arg_as_subject: str,
             file: Filename):

    entry = f"{count}/{total_mssgs}"
    body = mssg_body(file)
    #return json.dumps({
    return {"entry":  entry,
            "subject": str_arg_as_subject,
            "content": body
            }, indent=4)            

def txtPayload(metadata: dict):# entry, timestamp, txt_mssg):
    return json.dumps(metadata)
  #TODO: txtPayload might not be required at all.
