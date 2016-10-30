def count_sort(unsorted_list, highest_score):
    score_to_counts = list()
    sorted_scores = list()
    score_to_counts = [0] * (highest_score+1)
    print score_to_counts
    for score in unsorted_list:
        score_to_counts[score]+=1
    print score_to_counts
    for score, occurrence in enumerate(score_to_counts):
        if occurrence!=0:
            for x in range(occurrence):#append as many times it occurs
                sorted_scores.append(score)
    print sorted_scores[::-1]
#driver
unsorted_list = [2,0,4,14,5,1,0,74,0,16,8,0,9]
count_sort(unsorted_list, 99)
