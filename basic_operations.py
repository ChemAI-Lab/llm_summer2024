import numpy as np 
import argparse

def basic_operation(operation: str = 'times', first: int=1, second: float=10.): 
    A = 0.0 
    if operation == 'times':
        A = first * second 
    elif operation== 'div':
        A = first / second
    return print(A) 

def main():
    parser = argparse.ArgumentParser(description="Baisc Operation")
    parser.add_argument("--op", type=str, default='div',
                        help="operation")
    parser.add_argument("--fst", type=int,default=1,
                        help="first term")
    parser.add_argument("--sec", type=float, default=10.,
                         help="second term")
    
    args = parser.parse_args()
    
    op = args.op
    first = args.fst
    second = args.sec
    
    basic_operation(op,first,second) 

if __name__ == "__main__":
    main()
