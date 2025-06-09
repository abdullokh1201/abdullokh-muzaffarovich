#1.

customer_total = df4.groupby('Customer_ID')['Total_Price'].sum().reset_index()
customer_total.columns = ['Customer_ID', 'Total_Spent']

top_customers = customer_total.sort_values(by='Total_Spent', ascending=False).head(5)

customer_info = pd.DataFrame({
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Name': ['Anna', 'Brian', 'Cathy', 'Dan', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Jane']
})

top_customers_named = pd.merge(top_customers, customer_info, on='Customer_ID')
top_customers_named = top_customers_named[['Customer_ID', 'Name', 'Total_Spent']]
print(top_customers_named)


print(top_customers)

#2.

purchases_df = pd.DataFrame({
    'Customer_ID': [1, 1, 2, 2, 2, 3, 4, 4, 5],
    'Album_ID': ['A1', 'A1', 'A1', 'A2', 'A2', 'A1', 'A2', 'A2', 'A3'],
    'Track_ID': ['T1', 'T2', 'T1', 'T3', 'T4', 'T3', 'T3', 'T4', 'T5']
})

album_tracks_df = pd.DataFrame({
    'Album_ID': ['A1', 'A1', 'A1', 'A2', 'A2', 'A3'],
    'Track_ID': ['T1', 'T2', 'T3', 'T3', 'T4', 'T5']
})

album_track_counts = album_tracks_df.groupby('Album_ID')['Track_ID'].nunique().reset_index()
album_track_counts.columns = ['Album_ID', 'Total_Tracks']

customer_album_track_counts = purchases_df.groupby(['Customer_ID', 'Album_ID'])['Track_ID'].nunique().reset_index()
customer_album_track_counts.columns = ['Customer_ID', 'Album_ID', 'Tracks_Purchased']

merged = pd.merge(customer_album_track_counts, album_track_counts, on='Album_ID')
merged['Purchase_Type'] = merged.apply(
    lambda row: 'Full Album' if row['Tracks_Purchased'] == row['Total_Tracks'] else 'Individual Tracks',
    axis=1
)

customer_preference = merged.groupby('Customer_ID')['Purchase_Type'].apply(lambda x: 'Full Album' if all(x == 'Full Album') else 'Individual Tracks').reset_index()
customer_preference.columns = ['Customer_ID', 'Preference']

summary = customer_preference['Preference'].value_counts(normalize=True) * 100
print(summary.round(2))

Individual Tracks    60.0
Full Album           40.0
Name: Preference, dtype: float64


