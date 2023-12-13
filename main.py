import os
import sys

from PIL import Image
import imagehash
import pickle

# Load db if it exists. If not, generate it from fb inbox.
if os.path.isfile("db.pickle"):
    with open("db.pickle", "rb") as f:
        db = pickle.load(f)
else:
    db = []
    for file in os.listdir("/Users/osnr/Dropbox/fb/messages/inbox/disneyland1_1hkorraw0w/photos"):
        filename = os.fsdecode(file)
        p = "/Users/osnr/Dropbox/fb/messages/inbox/disneyland1_1hkorraw0w/photos/" + filename

        db.append((p, imagehash.average_hash(Image.open(p))))
    with open("db.pickle", "wb") as f:
        pickle.dump(db, f)

if len(sys.argv) == 2:
    print(sys.argv[1])
    imhash = imagehash.average_hash(Image.open(sys.argv[1]))
    print(imhash)

    # sort db by closeness to hash
    db_by_closeness = sorted(db, key=lambda im: im[1] - imhash)
    print(db_by_closeness[0][0])
    print(db_by_closeness[1][0])
    print(db_by_closeness[2][0])

    print("Least similar:")
    print(db_by_closeness[-1][0])
    print(db_by_closeness[-2][0])
    
    exit(0)

