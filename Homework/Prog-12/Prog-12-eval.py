data0 = read_data('data0.csv')
data1 = read_data('data1.csv')
data2 = read_data('data2.csv')
data3 = read_data('data3.csv')
assert max_new_cases_date(data0) == ('2021-03-13', 21578)
assert max_new_cases_date(data1) == ('2021-03-02', 531)
assert max_new_cases_date(data3) == ('2021-05-01', 279)
 	 
assert max_new_cases_province(data0, '2021-03-01', '2021-03-16') == ('P41', 5043)
assert max_new_cases_province(data0, '2021-03-12', '2021-03-15') == ('P69', 1786)
assert max_new_cases_province(data1, '2021-03-01', '2021-03-06') == ('D', 410)
assert max_new_cases_province(data1, '2021-03-02', '2021-03-05') == ('C', 313)
assert max_new_cases_province(data2, '2021-03-01', '2021-03-06') == ('E', 183)
assert max_new_cases_province(data2, '2021-03-02', '2021-03-05') == ('R', 125)
assert max_new_cases_province(data3, '2021-04-29', '2021-05-04') == ('E', 183)
assert max_new_cases_province(data3, '2021-04-30', '2021-05-03') == ('R', 125)
 	 
assert (max_new_cases_province_by_dates(data0) == np.array([
['2021-03-01', 'P48', 490],      
['2021-03-02', 'P38', 499],      
['2021-03-03', 'P20', 484],      
['2021-03-04', 'P56', 497],      
['2021-03-05', 'P58', 500],      
['2021-03-06', 'P66', 499],      
['2021-03-07', 'P28', 498],      
['2021-03-08', 'P70', 498],      
['2021-03-09', 'P10', 494],      
['2021-03-10', 'P45', 496],      
['2021-03-11', 'P74', 491],      
['2021-03-12', 'P74', 495],      
['2021-03-13', 'P18', 494],      
['2021-03-14', 'P27', 484],      
['2021-03-15', 'P64', 489],      
['2021-03-16', 'P34', 499]
],dtype=object)).all()
assert (max_new_cases_province_by_dates(data1) == np.array([
['2021-03-01', 'X', 60],      
['2021-03-02', 'C', 100],      
['2021-03-03', 'Y', 94],      
['2021-03-04', 'A', 94],      
['2021-03-05', 'E', 99],     
['2021-03-06', 'B', 89]
],dtype=object)).all()
assert (max_new_cases_province_by_dates(data3) == np.array([
['2021-04-29', 'E', 40],      
['2021-04-30', 'B', 39],      
['2021-05-01', 'R', 40],      
['2021-05-02', 'R', 40],      
['2021-05-03', 'Q', 35],      
['2021-05-04', 'S', 46]
],dtype=object)).all()
 	 
assert most_similar(data0, 'X') == 'B'
assert most_similar(data1, 'X') == 'B'
assert most_similar(data3, 'X') == 'Y' 
 	 
assert most_similar_province_pair(data0) == ('P38', 'P61')
assert most_similar_province_pair(data1) == ('C', 'D')
assert most_similar_province_pair(data3) == ('Y', 'W') 
 	 
assert most_similar_in_period(data0, 'X', '2021-03-01', '2021-03-16') == ('B', '2021-03-01', '2021-03-16')
assert most_similar_in_period(data0, 'X', '2021-03-12', '2021-03-15') == ('P58', '2021-03-01', '2021-03-04')
assert most_similar_in_period(data0, 'B', '2021-03-12', '2021-03-15') == ('P64', '2021-03-09', '2021-03-12')
assert most_similar_in_period(data1, 'X', '2021-03-01', '2021-03-06') == ('B', '2021-03-01', '2021-03-06')
assert most_similar_in_period(data1, 'X', '2021-03-02', '2021-03-05') == ('E', '2021-03-03', '2021-03-06')
assert most_similar_in_period(data1, 'B', '2021-03-02', '2021-03-05') == ('D', '2021-03-03', '2021-03-06')
assert most_similar_in_period(data2, 'X', '2021-03-01', '2021-03-06') == ('Y', '2021-03-01', '2021-03-06')
assert most_similar_in_period(data2, 'X', '2021-03-02', '2021-03-05') == ('Y', '2021-03-03', '2021-03-06')
assert most_similar_in_period(data2, 'B', '2021-03-02', '2021-03-05') == ('P', '2021-03-03', '2021-03-06')
assert most_similar_in_period(data3, 'X', '2021-04-29', '2021-05-04') == ('Y', '2021-04-29', '2021-05-04')
assert most_similar_in_period(data3, 'X', '2021-04-30', '2021-05-03') == ('Y', '2021-05-01', '2021-05-04')
assert most_similar_in_period(data3, 'B', '2021-04-30', '2021-05-03') == ('P', '2021-05-01', '2021-05-04')