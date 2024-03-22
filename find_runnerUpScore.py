if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    sorted_arr=sorted(arr)
    unique=list(set(sorted_arr))
    print(unique[-2])
    
