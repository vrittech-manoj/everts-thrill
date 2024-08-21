import pandas as pd
import json

# Create a sample DataFrame with the required fields according to the API
data = {
    'destination_title': ['Everest Base Camp', 'Annapurna Circuit'],
    'itinerary': ['Day 1: Arrival, Day 2: Trekking', 'Day 1: Start Trek, Day 2: Continue Trek'],
    'duration': [14, 21],
    'trip_grade': ['Challenging', 'Moderate'],
    'max_altitude': [5364, 5416],
    'meals': ['Breakfast, Lunch, Dinner', 'Breakfast, Lunch, Dinner'],
    'nature_of_trip': ['Adventure', 'Cultural'],
    'accommodation': ['Teahouse, Hotel', 'Teahouse, Lodge'],
    'group_size': [10, 15],
    'Featured Image Link': [
        'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c',
        'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c'
    ],
    'Packages': [
        json.dumps(['phone', 'supreme']),
        json.dumps(['phone', 'supreme'])
    ],
    'Gallery Image Links': [
        json.dumps([
           'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c',
            'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c'
        ]),
        json.dumps([
            'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c',
            'https://drive.google.com/uc?export=view&id=1RH59AxD_xFGaDx1ViFvxrQK1zq1KVd9c'
        ])
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file_path = 'trek/utilities/test.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Test Excel file created at: {excel_file_path}")
