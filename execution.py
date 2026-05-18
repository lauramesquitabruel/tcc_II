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
                        help='can represent the first of the tests to be run [1-80] or the size of the input strings')
    parser.add_argument('lst', type=int, choices=range(0,145), metavar='lst',
                        help='can represent the last of the tests to be run [1-80] or be 0')

    args = parser.parse_args()
    return args

def main():
    args = _parse_args()
    if args.lst != 0:
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

                file_path = Path(f"logs/cg/{filename}.txt")
                file_path.parent.mkdir(parents=True, exist_ok=True)

                #print(filename)
                solve(s1, s2, alfabeto, file_path)
                #teste(s1, s2, alfabeto)

    else:
        pattern = re.compile(rf"rmcsp_{args.fst}_\d+_(\d+)_([-+]?\d*\.?\d*)-")
        input_dir = Path('instances_new')
        log_dir = Path('logs/cg')

        for file_path in input_dir.glob("rmcsp_*.in"):
            match = pattern.search(file_path.name)
            if match:
                filename_stem = file_path.stem
            
                with open(file_path, 'r') as f:
                    alfabeto = int(f.readline().split()[1])
                    s1 = list(map(int, f.readline().split()))
                    s2 = list(map(int, f.readline().split()))

                    log_path = log_dir / f"{filename_stem}.txt"
                    log_path.parent.mkdir(parents=True, exist_ok=True)

                    #print(filename_stem)
                    solve(s1, s2, alfabeto, log_path)
               

main()
