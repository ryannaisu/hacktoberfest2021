def decToBiner(num):
    result=""
    while num >= 1:
        num = num // 2
        result=result+str(num % 2)
    print(result[::-1])

if __name__ == '__main__':
    try:
        inputs = int(input("Input your number: "))
        decToBiner(inputs)
    except:
        print("There's an error occurred")