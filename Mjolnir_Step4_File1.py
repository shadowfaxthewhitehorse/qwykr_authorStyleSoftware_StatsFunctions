# STEP 4
#
# compute the following for every author
# [average_word_length, standard_deviation_of_word_length]
#
# DESCRIPTION:
#
# This program will take a document and compute:
# [average_word_length, standard_deviation_of_word_length]
# for the words in the document.
#
# EXAMPLE:
#
# If you have a short story, this program will compute the average word
# length of words in that short story, as well as the standard
# deviation of the word lengths of the words in that short story
#
# STEPS TO RUN THIS CODE:
#
# 1. Input data is to be kept in the directories indicated in inFilePath1 and InFilePath2.
#    Say, you want to compute these statistics for two short stories, one by Rider Haggard and
#    the other by (someone by the name of) Scully.
#
# 2. Run the code and it will tell you the average word lengths and the standard deviation of the
#    word lengths in the words in the short stories in question.
#
#
# HOW TO USE THIS CODE FOR MJOLNIR:
#
# 1. Take your generated output (after Steps 2 and 3 have been executed.) Run it through Step 4.
#
# 2. Take some sample representative writings of the author and run that also through Step 4.
#    (That is why I have inFilePath1 and InFilePath2.)
#
# 3. See if the generated output is at least within 0.25 or 0.5 standard deviations of what
#    it should be.
#

import statistics

myList1 = []

inFilePath1 = r"C:\Users\Anand Manikutty\PycharmProjects\Mjolnir_Step4\inputdata\RiderHaggard__LongOdds.txt";
inFilePath2 = r"C:\Users\Anand Manikutty\PycharmProjects\Mjolnir_Step4\inputdata\Scully__Ghamba.txt";

outFilePath = r"C:\Users\Anand Manikutty\PycharmProjects\Mjolnir_Step4\outputdata\statistics_op1.txt";

myinfile1 = open(inFilePath1,"r")
myinfile2 = open(inFilePath2,"r")

myoutfile = open(outFilePath, "w+")

if (myinfile1.mode == 'r'):
    # read the file - line by line

    for line in myinfile1:

        fresh_list = []
        splits = line.split()
        for word in splits:
            fresh_list.append(len(word))

        myList1.extend(fresh_list)

list_average = statistics.mean(myList1)
list_std_deviation = statistics.stdev(myList1)

print(list_average)
print(list_std_deviation)

myoutfile.write("AVERAGE = " + str(float(list_average)) + "; STANDARD DEVIATION =" + str(float(list_std_deviation)))

myinfile1.close()

myinfile2.close()

myoutfile.close()

