def open_read_file(file):
    f = open(file, "r")
    print (type(f))

    count = 0
    line = f.readline()
    while line:
        print(line, end= '') 
        line = f.readlines()

        cnt += 1
    print("")
    print('there are', cnt, 'lines in the file')
    f.close() 
def main():
    open_read_file('ghh.txt')

if __name__ == '__main__':
    main()
    
    
    