# python3

def parallel_processing(n, data):
    work_time = []
    for i in range(n):
        work_time.append(0)

    seconds = 0
    index = 0
    while True:
        for i in range(n):
            if work_time[i] == 0:
                work_time[i] = data[index]
                index += 1
                print(str(i) + " " + str(seconds))
                if index >= len(data):
                    return

        for i in range(n):
            work_time[i] += -1

        seconds += 1


def main():
    variables = list(map(int, input().split()))
    n = variables[0]
    m = variables[1]
    data = list(map(int, input().split()))

    parallel_processing(n, data)



if __name__ == "__main__":
    main()
