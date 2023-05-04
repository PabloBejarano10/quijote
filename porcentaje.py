import random
import sys
def main(infilename, outfilename, porcentaje):
    with open(infilename) as infile:
        with open(outfilename, 'w') as outfile:
            for line in infile:
                if random.random()<=porcentaje:
                    outfile.write(line)


if __name__=="__main__":
    if len(sys.argv)<4:
        print(f"Usage: {sys.argv[0]} <infilename> <outfilename> <porcentaje>")
        exit(1)
    infilename = sys.argv[1]
    outfilename = sys.argv[2]
    porcentaje = float(sys.argv[3])
    main(infilename, outfilename, porcentaje)
