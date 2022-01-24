
#Since 'gross' and 'budget' columns have many NaN values, drop all the rows with NaNs at this column using the isnan() function of NumPy along with a negation ~
data = data[~np.isnan(data['gross'])]
data = data[~np.isnan(data['budget'])]

#Let's retain the rows which have less than two sums of null
data = data[data.isnull().sum(axis=1) <= 2]
data.isnull().sum()
