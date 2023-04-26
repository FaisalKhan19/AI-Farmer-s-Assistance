import pandas as pd
crop_dict = {
    "Alluvial": ["Rice", "Banana", "Sugarcane", "Tobacco", "Wheat", "Barley", "Peas & beans (Pulses)", "Paddy", "Tea", "Coffee", "Apple", "Peach", "Pear", "Plums", "Litchi"],
    "Black": ["Cotton(lint)", "Urad", "Arhar/Tur", "Groundnut", "Onion", "Sesamum", "Linseed", "Safflower", "Rapeseed &Mustard", "Jute", "Bitter Gourd", "Drum Stick", "Jack Fruit", "Snak Guard", "Pump Kin", "Other Dry Fruit"],
    "Red": ["Arecanut", "Dry ginger", "Turmeric", "Gram", "Masoor", "Coriander", "Potato", "Soyabean", "Beans & Mutter(Vegetable)", "Bhindi", "Brinjal", "Citrus Fruit", "Cucumber", "Grapes", "Mango", "Orange", "Papaya", "Pome Fruit", "Tomato", "Cabbage", "Peas  (vegetable)", "Bottle Gourd", "Garlic", "Ginger", "Water Melon", "Colocosia", "Lentil", "Bean", "Jobster", "Perilla", "Rajmash Kholar", "Ricebean (nagadal)", "Ash Gourd", "Beet Root", "Lab-Lab", "Ribed Guard", "Yam"],
    "Clay": ["Other Kharif pulses", "Cashewnut", "Coconut", "Dry chillies", "other oilseeds", "Maize", "Moong(Green Gram)", "Sunflower", "Bajra", "Castor seed", "Horse-gram", "Jowar", "Korra", "Ragi", "Gram", "Sesamum", "Linseed", "Safflower", "other misc. pulses", "Samai", "Small millets", "Other  Rabi pulses", "Cauliflower", "Other Citrus Fruit"]
}

soil_type = ["Alluvial","Black","Red","Clay"]


def make_data(district, season, label, area):
    soil = soil_type[label-1]
    crops = crop_dict[soil]
    df = pd.read_csv("C:\\Users\\Faisal Ali khan\\Desktop\\Flask 2\\VENV\\Models\\input.csv")
    cols = df.columns
    for crop in crops:
        new_row = {}
        for col in cols:
            if 'area' in col.lower():
                new_row[col] = area
            elif 'district' in col.lower():
                new_row[col] = 1 if district.upper() in col.upper() else 0
            elif 'season' in col.lower():
                new_row[col] = 1 if season.upper() in col.upper() else 0
            elif 'crop' in col.lower():
                new_row[col] = 1 if crop.upper() in col.upper() else 0
            else:
                new_row[col] = 0
        new_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_df], ignore_index=True)
    
    return df.drop('Unnamed: 0',axis=1)
    
def map_yeilds(pred, label):
    soil = soil_type[label-1]
    crops = crop_dict[soil]
    yeilds = dict(zip(crops, pred))
    return yeilds