from __future__ import print_function

def encode(input):
    prev_char = input[0]
    curr_char = input[1]
    curr_len = 1
    output = [[prev_char,curr_len]];

    for i in range(1,len(input)):
        curr_char = input[i]
        if prev_char == curr_char:
            output[len(output)-1][1]+=1
        else:
            output.append([curr_char,1])
        prev_char = curr_char

    for i in range(len(output)):
        print(output[i][1],end='')
        print(output[i][0],end='')
    print('');


def main():
    test = raw_input("input : ")
    encode(test)

if __name__ == "__main__":
    main()
