def count_sort(unsorted_list, highest_score):
    score_to_counts = list()
    sorted_scores = list()
    score_to_counts = [0] * (highest_score+1)
    for score in unsorted_list:
        score_to_counts[score]+=1
    for score, occurrence in enumerate(score_to_counts):
        if occurrence!=0:
            for x in range(occurrence):
                sorted_scores.append(score)
    print sorted_scores
#driver
unsorted_list = [33,2,35,26,47,89,41,13,89,99]
count_sort(unsorted_list, 99)
