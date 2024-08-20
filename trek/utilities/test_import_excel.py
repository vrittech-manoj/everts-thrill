import pandas as pd

# Create sample data for the destination Excel file
destination_data = {
    "Destination Title": ["Everest Base Camp", "Annapurna Circuit", "Langtang Valley", "Manaslu Circuit"],
    "Price": [1500, 1200, 1000, 1300],
    "Price Type": ["USD", "USD", "USD", "USD"],
    "Is Price": [True, True, True, True],
    "Overview": [
        "A trek to the base camp of the world's highest mountain, Mount Everest.",
        "A trek around the Annapurna massif, crossing the Thorong La pass.",
        "A beautiful trek in the Langtang region, offering stunning views of the valley and surrounding peaks.",
        "A challenging trek around Manaslu, the eighth highest mountain in the world."
    ],
    "Inclusion and Exclusion": [
        "Includes guide, porter, permits; excludes personal expenses, travel insurance.",
        "Includes meals, accommodation, guide; excludes international flights.",
        "Includes transportation, meals, permits; excludes tips, personal gear.",
        "Includes full-board accommodation, guide; excludes visa fees, insurance."
    ],
    "Itinerary": [
        "Day 1: Arrival in Kathmandu\nDay 2: Flight to Lukla and trek to Phakding\nDay 3: Trek to Namche Bazaar",
        "Day 1: Arrival in Kathmandu\nDay 2: Drive to Besishahar and trek to Chame\nDay 3: Trek to Pisang",
        "Day 1: Arrival in Kathmandu\nDay 2: Drive to Syabrubesi\nDay 3: Trek to Lama Hotel",
        "Day 1: Arrival in Kathmandu\nDay 2: Drive to Soti Khola\nDay 3: Trek to Machha Khola"
    ],
    "Trip Map URL": [
        "https://example.com/everest-map",
        "https://example.com/annapurna-map",
        "https://example.com/langtang-map",
        "https://example.com/manaslu-map"
    ],
    "Duration": [14, 18, 10, 16],
    "Trip Grade": ["Strenuous", "Moderate", "Moderate", "Challenging"],
    "Best Season": ["Spring, Autumn", "Spring, Autumn", "Spring, Autumn", "Spring, Autumn"],
    "Max Altitude": ["5,364m", "5,416m", "3,870m", "5,135m"],
    "Meals": [
        "Breakfast, Lunch, Dinner",
        "Breakfast, Lunch, Dinner",
        "Breakfast, Lunch, Dinner",
        "Breakfast, Lunch, Dinner"
    ],
    "Nature of Trip": ["Trekking", "Trekking", "Trekking", "Trekking"],
    "Accommodation": ["Lodge/Teahouse", "Lodge/Teahouse", "Lodge/Teahouse", "Lodge/Teahouse"],
    "Group Size": [12, 15, 10, 8],
    "Gallery Images Links": [
        "https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing, https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing",
        "https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing, https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing",
        "https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing, https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing",
        "https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing, https://drive.google.com/file/d/1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj/view?usp=sharing"
    ]
}

# Create a DataFrame for the destination data
destination_df = pd.DataFrame(destination_data)

# Save the destination data to an Excel file
destination_file_path = 'trek/utilities/sample_destination_data.xlsx'
destination_df.to_excel(destination_file_path, index=False)

# Create sample data for the packages Excel file
package_data = {
    "Package Name": ["Everest Base Camp Package", "Annapurna Circuit Package", "Langtang Valley Package", "Manaslu Circuit Package"],
    "Description": [
        "Everest Base Camp trek package",
        "Annapurna Circuit trek package",
        "Langtang Valley trek package",
        "Manaslu Circuit trek package"
    ],
    "Price": [1500, 1200, 1000, 1300]
}

# Create a DataFrame for the package data
package_df = pd.DataFrame(package_data)

# Save the package data to an Excel file
package_file_path = 'trek/utilities/sample_package_data.xlsx'
package_df.to_excel(package_file_path, index=False)

(destination_file_path, package_file_path)
