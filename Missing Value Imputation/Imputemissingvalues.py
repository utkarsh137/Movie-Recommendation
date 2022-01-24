# for numerical column we use mean() function
data['num_critic_for_reviews'].fillna(data['num_critic_for_reviews'].mean(), inplace = True)
data['duration'].fillna(data['duration'].mean(), inplace = True)

# for categorical column we use mode() function
data['language'].fillna(data['language'].mode()[0], inplace = True)

# for actor name column

data['actor_2_name'].fillna('Unknown Actor', inplace = True)
data['actor_3_name'].fillna('Unknown Actor', inplace = True)

# as we imputed all the missing values lets check the no. of total missing values in the dataset
print('Total missing values after Imputation :', data.isnull().sum().sum())
