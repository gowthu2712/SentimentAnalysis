import math
import string

def Naive_Bayes_Classifier(positive, negative, total_negative, total_positive, test_string):
    y_values = [0,1]
    prob_values = [None, None]

    for y_value in y_values:
        posterior_prob = 1.0

        for word in test_string.split():
            word = word.lower().translate(None,string.punctuation).strip()
            if y_value == 0:
                if word not in negative:
                    posterior_prob *= 0.0
                else:
                    posterior_prob *= negative[word]
            else:
                if word not in positive:
                    posterior_prob *= 0.0
                else:
                    posterior_prob *= positive[word]

        if y_value == 0:
            prob_values[y_value] = posterior_prob * float(total_negative) / (total_negative + total_positive)
        else:
            prob_values[y_value] = posterior_prob * float(total_positive) / (total_negative + total_positive)

    total_prob_values = 0
    for i in prob_values:
        total_prob_values += i

    for i in range(0,len(prob_values)):
        prob_values[i] = float(prob_values[i]) / total_prob_values

    print prob_values

    if prob_values[0] > prob_values[1]:
        return 0
    else:
        return 1


if __name__ == '__main__':
    AMAZON_FILE = open("/amazon_cells_labelled.txt")
    YELP_FILE = open("/yelp_labelled.txt")
    IMDB_FILE = open("/imdb_labelled.txt")


    #Preprocessing of training set
    vocabulary = {}
    positive = {}
    negative = {}
    training_set = []
    TOTAL_WORDS = 0
    total_negative = 0
    total_positive = 0

    for line in AMAZON_FILE:
        words = line.split()
        y = words[-1].strip()
        y = int(y)

        if y == 0:
            total_negative += 1
        else:
            total_positive += 1

        for word in words:
            word = word.lower().translate(None,string.punctuation).strip()
            if word not in vocabulary and word.isdigit() is False:
                vocabulary[word] = 1
                TOTAL_WORDS += 1
            elif word in vocabulary:
                vocabulary[word] += 1
                TOTAL_WORDS += 1

            #Training
            if y == 0:
                if word not in negative:
                    negative[word] = 1
                else:
                    negative[word] += 1
            else:
                if word not in positive:
                    positive[word] = 1
                else:
                    positive[word] += 1

    for line in YELP_FILE:
        words = line.split()
        y = words[-1].strip()
        y = int(y)

        if y == 0:
            total_negative += 1
        else:
            total_positive += 1

        for word in words:
            word = word.lower().translate(None,string.punctuation).strip()
            if word not in vocabulary and word.isdigit() is False:
                vocabulary[word] = 1
                TOTAL_WORDS += 1
            elif word in vocabulary:
                vocabulary[word] += 1
                TOTAL_WORDS += 1

            #Training
            if y == 0:
                if word not in negative:
                    negative[word] = 1
                else:
                    negative[word] += 1
            else:
                if word not in positive:
                    positive[word] = 1
                else:
                    positive[word] += 1

    for line in IMDB_FILE:
        words = line.split()
        y = words[-1].strip()
        y = int(y)

        if y == 0:
            total_negative += 1
        else:
            total_positive += 1

        for word in words:
            word = word.lower().translate(None,string.punctuation).strip()
            if word not in vocabulary and word.isdigit() is False:
                vocabulary[word] = 1
                TOTAL_WORDS += 1
            elif word in vocabulary:
                vocabulary[word] += 1
                TOTAL_WORDS += 1

            #Training
            if y == 0:
                if word not in negative:
                    negative[word] = 1
                else:
                    negative[word] += 1
            else:
                if word not in positive:
                    positive[word] = 1
                else:
                    positive[word] += 1


    for word in vocabulary.keys():
        vocabulary[word] = float(vocabulary[word])/TOTAL_WORDS

    for word in positive.keys():
        positive[word] = float(positive[word])/total_positive

    for word in negative.keys():
        negative[word] = float(negative[word])/total_negative

    test_string = raw_input("Enter the review: \n")

    classifier = Naive_Bayes_Classifier(positive, negative, total_negative, total_positive, test_string)
    if classifier == 0:
        print "Negative review"
    else:
        print "Positive review"
