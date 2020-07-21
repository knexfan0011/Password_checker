import hashlib
import time

debug = False  # Flag to toggle debug outputs
while True:
    print("------------------------")

    a = input("Check Password: ")
    hash_capitalized = hashlib.sha1(a.encode()).hexdigest().upper()
    a = None
    if debug:
        print("Corresponding Hash: "+hash_capitalized)
        print("Comparing...")

    starttime = time.time()
    chars = hash_capitalized[0:3]
    if debug:
        print("Checking file "+chars+"_hashes.txt")
    file = open("Lookup_files/"+chars+"_hashes.txt", "r")
    hash_found = False

    for line in file:
        hash = line.split(":")[0]
        if hash == hash_capitalized:
            print("This hash has been pwned "+(line.split(":")[1]).split("\n")[0]+" times")
            hash_found = True
            break
    if not hash_found:
        print("This hash has never been pwned")
