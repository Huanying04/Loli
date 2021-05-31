import sys
from os import path

import runner

version = '1.2.0'


def main(args):
    if args[0] == '-file' or args[0] == '-f':
        if path.exists(args[1]):
            runner.run(runner.read(args[1]), True, False, 0)
        else:
            print('The file is not exist')
    elif args[0] == '-?' or args[0] == '-help':
        print(f'Loli ver{version}\n'
              'by: 貓村幻影\n'
              '\n'
              '-?                        顯示這段文字\n'
              '-help                     同-?\n'
              '-file <filepath>          執行原始碼\n'
              '-f <filepath>             同-file\n')
    else:
        print('Unknown param, plz use "loli -?" for more help')
    return


if __name__ == '__main__':
    if len(sys.argv) >= 2:
        main(sys.argv[1:])
    else:
        print(f'Loli ver {version}\nby: 貓村幻影\nType "loli - ?" for more help')
