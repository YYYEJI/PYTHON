### YOUR CODE STARTS HERE
# This list contains characters to divide words for each file.
sp = [',', ';', ' ', '	', '	', ',', ';', ' ', '/']
# This line has a list of the number of ENFJs in each file.
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# This line is a for statement that will turn 9 times.
for i in range(9):
    # This line is the name of the file.
    MBTI_center = "/Users/song-yeji/Desktop/p/A08_22100396/MBTI-center-"
    # This line gives the file an additional name.
    MBTI_center = MBTI_center + str(i) + ".txt"

    # This line opens the file for read.
    file = open(MBTI_center, "rt")
    
    # This line turns while statement.
    while True:
        # This line reads the file.
        f = file.readline()
        # If nothing is read from the file,
        if f == '':
            # exits while statement.
            break
        # This line distributes the contents of the file you read by letter.
        mbti_result = f.split(sp[i])

    # This line reads the list one by one.
    for enfj in mbti_result:
        # If the word is ENFJ or ENXJ,
        if enfj == "ENFJ" or enfj == "ENXJ":
            # increase the number by one.
            cnt[i] = cnt[i] + 1
    
    # This line closes the file.
    file.close()

# This line is a for statement that will turn 9 times.
for i in range(9):
    # This line opens the file for write.
    f = open('/Users/song-yeji/Desktop/p/A08_22100396/results.txt', 'a')
    # This line stores the results in variables according to the given format.
    result = str(i) + "," + str(cnt[i]) + "\n" 
    # This line wirtes the results in the results.txt file.
    f.write(result)

# This line closes the file.
f.close()
    

### YOUR CODE ENDS HERE