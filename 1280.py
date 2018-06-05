def main():
    before = [None]*(100000 + 1)
    after = [None]*(100000 + 1)
    orders = [None]*(1000 + 1)

    numOfSubjects, numOfLimitations = input().split()
    numOfSubjects = int(numOfSubjects)
    numOfLimitations = int(numOfLimitations)

    for indexOfLimitation in range(1, numOfLimitations+1):
        before[indexOfLimitation], after[indexOfLimitation] = input().split()
        before[indexOfLimitation] = int(before[indexOfLimitation])
        after[indexOfLimitation] = int(after[indexOfLimitation])

    subject = input().split()
    for indexOfSubject in range(1, numOfSubjects+1):
        orders[int(subject[indexOfSubject-1])] = indexOfSubject

    isCorrect = True
    for indexOfLimitation in range(1, numOfLimitations+1):
        if orders[before[indexOfLimitation]] > orders[after[indexOfLimitation]]:
            isCorrect = False
            break

    if isCorrect:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
