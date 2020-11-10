import pandas as pd

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 50)

# Load csv data into Pandas dataframe.
def load_data(filename):
	return pd.read_csv(filename, encoding='utf-8')

# Remove unimportant columns.
def remove_uneccessary_columns(data):
	"""Given a filename of a csv load data into a Pandas dataframe.

        filename - string

        return Pandas dataframe
	"""
	data.drop(["branch", "model", "candidate_3rd", "ecwin_3rd"], axis=1, inplace=True)

def main():
	data = load_data('presidential_national_toplines_2020.csv')
	remove_uneccessary_columns(data)

	data.to_csv('clean_data.csv', encoding='utf-8', index=False)


if __name__ == '__main__':
	main()