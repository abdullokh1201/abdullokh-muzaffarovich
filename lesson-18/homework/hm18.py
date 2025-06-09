#1.

import pandas as pd

# Загрузка CSV
df = pd.read_csv('questions.csv', sep='\t', parse_dates=['creationdate'])

# Убедимся, что имена колонок не содержат пробелов и всё в нижнем регистре
df.columns = df.columns.str.strip().str.lower()

before_2014 = df[df['creationdate'] < '2014-01-01']
print(before_2014)

score_over_50 = df[df['score'] > 50]
print(score_over_50)

score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(score_between_50_100)

answered_by_scott = df[df['ans_name'].str.lower() == 'scott boston']
print(answered_by_scott)

users = ['unutbu', 'scott boston', 'mike pennington', 'doug', 'demitri']
answered_by_five = df[df['ans_name'].str.lower().isin(users)]
print(answered_by_five)

mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'].str.lower() == 'unutbu') &
    (df['score'] < 5)
)
filtered = df[mask]
print(filtered)

filtered = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print(filtered)

not_by_scott = df[df['ans_name'].str.lower() != 'scott boston']
print(not_by_scott)

#2.

import pandas as pd

# Загрузка данных
titanic_df = pd.read_csv("task/titanic.csv")

female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20, 30))
]

fare_over_100 = titanic_df[titanic_df['Fare'] > 100]

survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

embarked_c_fare_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]


with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

under_15_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 0)
]

with_cabin_fare_200 = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]

odd_id_passengers = titanic_df[titanic_df['PassengerId'] % 2 != 0]

ticket_counts = titanic_df['Ticket'].value_counts()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_passengers = titanic_df[titanic_df['Ticket'].isin(unique_tickets)]

miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss', case=False, na=False)) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == 'female')
]




