from .cli import hello
import argparse

def main():
    parser = argparse.ArgumentParser(description='A simple CLI program')
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    hello(args)

if __name__ == '__main__':
    main()
