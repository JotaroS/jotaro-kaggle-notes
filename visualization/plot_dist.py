import matplotlib.pyplot as plt

def plot_dist_col_train_test(train_df, test_df, column):
    '''plot dist curves for train and test weather data for the given column name'''
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.distplot(train_df[column].dropna(), color='green', ax=ax).set_title(column, fontsize=16)
    sns.distplot(test_df[column].dropna(), color='purple', ax=ax).set_title(column, fontsize=16)
    plt.xlabel(column, fontsize=15)
    plt.legend(['train', 'test'])
    plt.show()
    return plt