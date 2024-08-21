import pandas as pd
import json

# Sample data for destinations with explicit image links
data = [
    {
        "destination_title": "Everest Base Camp Trek",
        "price": 1200.0,
        "price_type": "USD",
        "is_price": True,
        "overview": "A challenging trek to the base of the world's highest mountain.",
        "ltinerary": "Day 1: Arrival in Kathmandu, Day 2: Fly to Lukla and trek to Phakding...",
        "duration": 14,
        "trip_grade": "Strenuous",
        "max_altitude": "5545m",
        "meals": "Breakfast, Lunch, Dinner",
        "nature_of_trip": "Trekking",
        "accommodation": "Tea houses",
        "group_size": 12,
        "gear_and_equipment": "Trekking boots, Down jacket, Sleeping bag...",
        "useful_information": "Best time to visit is March to May and September to November.",
        "trip_map_url": "https://maps.example.com/everest_base_camp_trek",
        "featured_image_link": "https://drive.google.com/uc?id=1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for featured image
        "gallery_image_links": json.dumps([
            "https://drive.google.com/uc?id=1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for gallery image 1
            "https://drive.google.com/uc?id=1fZgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for gallery image 2
        ]),
        "packages": json.dumps(["supreme", "phone"])  # Replace with actual package names
    },
    {
        "destination_title": "Annapurna Circuit Trek",
        "price": 1500.0,
        "price_type": "USD",
        "is_price": True,
        "overview": "A scenic trek through the Annapurna range.",
        "ltinerary": "Day 1: Arrival in Kathmandu, Day 2: Drive to Besishahar...",
        "duration": 18,
        "trip_grade": "Moderate",
        "max_altitude": "5416m",
        "meals": "Breakfast, Lunch, Dinner",
        "nature_of_trip": "Trekking",
        "accommodation": "Tea houses",
        "group_size": 10,
        "gear_and_equipment": "Trekking poles, Down jacket, Rain gear...",
        "useful_information": "Best time to visit is October to November.",
        "trip_map_url": "https://maps.example.com/annapurna_circuit_trek",
        "featured_image_link": "https://drive.google.com/uc?id=1kZgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for featured image
        "gallery_image_links": json.dumps([
            "https://drive.google.com/uc?id=2jLgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for gallery image 1
            "https://drive.google.com/uc?id=3mHgLhtjYJSsvnLB46rA1gXdByOoH0cyj",  # Direct download link for gallery image 2
        ]),
        "packages": json.dumps(["supreme", "phone"])  # Replace with actual package names
    },
]

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file_path = 'trek/utilities/test.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"Test Excel file created at: {excel_file_path}")
