import argparse
import json
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
#mystor = "storage.json"

parse = argparse.ArgumentParser()
parse.add_argument("-k", "--key", type=str, help="Add keyword", default="")
parse.add_argument('-v', '--value', type=str, nargs="+",help="Add value ", default="")

args = parse.parse_args()

def isEmpty(myfile):
    with open(myfile, "r", encoding="utf-8") as f:
        if f.seek(0, os.SEEK_END):
            f.seek(0)
            return False            
        else:
            return True


tmpJsDict = None

def displayValue(k, myfile):
    if not isEmpty(myfile):
        with open(myfile, "r", encoding="utf-8") as f:
            tmpJsDict = json.load(f)
            if k in tmpJsDict.keys():
                print(", ".join(tmpJsDict[k]))
            else:
                print("")
    else:
        print(f"{myfile} is empty")


def saveKeyValue(k, v, myfile):
    tmpJsDict = dict()
    tmpJsDict[k] = v
    if isEmpty(myfile) :
        with open(myfile, "w", encoding="utf-8") as f:
            json.dump(tmpJsDict, f, indent=4)
    else:
        with open(myfile, "r", encoding="utf-8") as f:
            tmpJsDict = json.load(f)
        if k in tmpJsDict.keys():
            tmpJsDict[k].extend(v)
        else:
            tmpJsDict[k] = v
        with open(myfile, "w", encoding="utf-8") as f:
            json.dump(tmpJsDict, f, indent=4)
"""        """


        
if __name__ == "__main__":
    if args.key and args.value:
        saveKeyValue(args.key, args.value, storage_path)
    elif args.key:
        displayValue(args.key, storage_path)
        
