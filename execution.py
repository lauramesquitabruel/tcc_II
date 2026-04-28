import argparse
import os
import re
from pathlib import Path
from teste import teste
from solve import solve

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Runs ILP on selected UMCSP instances')
    parser.add_argument('fst', type=int, choices=range(1,145), metavar='fst',
                        help='first of the tests to be run [1-80]')
    parser.add_argument('lst', type=int, choices=range(1,145), metavar='lst',
                        help='last of the tests to be run [1-80]')
    args = parser.parse_args()
    return args

def main():
    args = _parse_args()
    if args.lst < args.fst:
        raise Exception('fst and lst must indicate a valid test range')
    
    for i in range(args.fst, args.lst + 1):
        filename = next(f
                    for f in os.listdir('instances')
                    if re.match(rf'rmcsp_0*{i}-', f))
        filename = Path(filename).stem
        with open(f'instances/{filename}.in') as f:
            alfabeto = int(f.readline().split()[1])
            s1 = list(map(int, f.readline().split()))
            s2 = list(map(int, f.readline().split()))

            #print(S, T, alfabeto)
            solve(s1, s2, alfabeto)
            #teste(s1, s2, alfabeto)

main()