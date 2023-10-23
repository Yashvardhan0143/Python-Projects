import math
import random  


def calculate_crop_damage():
    area_affected = float(input("Enter the affected area in acres: "))
    percentage_damage = float(input("Enter the percentage of damage: "))
    total_damage = (percentage_damage / 100) * area_affected
    print(f"Total crop damage is {total_damage} acres.")
    
    
def estimate_fertilizer_requirement():
    total_area = float(input("Enter the total area in acres: "))
    current_nutrient_level = float(input("Enter the current nutrient level: "))
    desired_nutrient_level = float(input("Enter the desired nutrient level: "))
    fertilizer_requirement = (desired_nutrient_level - current_nutrient_level) * total_area
    print(f"Fertilizer requirement is {fertilizer_requirement} units.")


def predict_crop_yield():
    area_under_cultivation = float(input("Enter the area under cultivation in acres: "))
    rainfall = float(input("Enter the rainfall in mm: "))
    temperature = float(input("Enter the average temperature in Celsius: "))
    crop_yield = (rainfall / 100) * (temperature / 30) * area_under_cultivation
    print(f"Predicted crop yield is {crop_yield} tons.")


def recommend_irrigation_schedule():
    last_week_rainfall = float(input("Enter the rainfall in the last week in mm: "))
    soil_moisture_level = float(input("Enter the soil moisture level: "))
    if last_week_rainfall < 20 and soil_moisture_level < 50:
        print("Recommendation: Irrigate the crops.")
    else:
        print("Recommendation: No immediate irrigation needed.")


def pest_control_recommendation():
    pest_severity = float(input("Enter pest severity level (0-10): "))
    crop_type = input("Enter crop type: ")
    if pest_severity > 5:
        print(f"Recommendation: Apply pest control for {crop_type}.")
    else:
        print("Recommendation: No immediate pest control needed.")


def more_details_recommendation():
    severity_level = float(input("Enter severity level (0-10): "))
    crop_type = input("Enter crop type: ")
    weather_conditions_type = input("Enter weather conditions type (e.g., Rainy, Sunny): ")
    if severity_level > 7 and "Rice" in crop_type and weather_conditions_type.lower() == "rainy":
        print("Recommendation: Consider implementing preventive measures for disease control.")
    else:
        print("Recommendation: No specific action recommended for the given conditions.")


def check_soil_health():
    soil_ph = round(random.uniform(4.5, 8.5), 2)  
    soil_nutrients = random.choice(["Low", "Medium", "High"]) 
    print(f"Soil Health Check:\n- Soil pH: {soil_ph}\n- Soil Nutrients: {soil_nutrients}")


def generate_crop_report():
    crop_name = input("Enter the crop name: ")
    crop_height = random.uniform(20, 200)  
    crop_yield = random.uniform(100, 1000) 
    print(f"Crop Report for {crop_name}:\n- Crop Height: {crop_height} cm\n- Crop Yield: {crop_yield} kg")
    
def calculate_harvest_time():
    growth_days = random.randint(60, 120)
    print(f"The estimated harvest time is {growth_days} days.")


def monitor_crop_growth():
    growth_rate = random.uniform(0.1, 1.0)  
    current_height = 10  
    days_elapsed = 0

    print("Monitoring Crop Growth:")
    while current_height < 150:
        days_elapsed += 1
        current_height *= (1 + growth_rate)
        print(f"Day {days_elapsed}: Crop height is {round(current_height, 2)} cm.")
        time.sleep(1)  


while True:
    print("\n1. Calculate Crop Damage")
    print("2. Estimate Fertilizer Requirement")
    print("3. Predict Crop Yield")
    print("4. Recommend Irrigation Schedule")
    print("5. Pest Control Recommendation")
    print("6. More Details and Recommendation")
    print("7. Check Soil Health")
    print("8. Generate Crop Report")
    print("9. Calculate Harvest Time")
    print("10. Monitor Crop Growth")
    print("11. Exit")

    choice = int(input("Enter your choice (1-11): "))

    if choice == 1:
        calculate_crop_damage()
    elif choice == 2:
        estimate_fertilizer_requirement()
    elif choice == 3:
        predict_crop_yield()
    elif choice == 4:
        recommend_irrigation_schedule()
    elif choice == 5:
        pest_control_recommendation()
    elif choice == 6:
        more_details_recommendation()
    elif choice == 7:
        check_soil_health()
    elif choice == 8:
        generate_crop_report()
    elif choice == 9:
        calculate_harvest_time()
    elif choice == 10:
        monitor_crop_growth()
    elif choice == 11:
        print("Exiting the program. Thank you!")
        print("Prepared by S.Mugundhan(RA2311003010549) and Nisanth.S(RA2311003010538)")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.")