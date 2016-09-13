from __future__ import print_function

global_output = []

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

    print('The encoded output is - ',end='')
    for i in range(len(output)):
        print(output[i][1],end='')
        print(output[i][0],end='')
    print('\n\n********************************************\ndecoding\n\n')

    input = ''
    for i in range(len(output)):
        for j in range(output[i][1]):
            input+=(output[i][0])
    print('The decoded input is - ',end='')
    print(input)

def main():
    while True:
        print('\n\n********************************************\ntype exit to leave program\n\n')
        input_string = raw_input("enter input : ")
        if(input_string == 'exit'):
            break
        print('\n\n')
        encode(input_string)


if __name__ == "__main__":
    main()
