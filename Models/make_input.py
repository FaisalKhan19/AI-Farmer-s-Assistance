crop_dict = {
    "Alluvial": ["Rice", "Banana", "Sugarcane", "Tobacco", "Wheat", "Barley", "Peas & beans (Pulses)", "Paddy", "Tea", "Coffee", "Apple", "Peach", "Pear", "Plums", "Litchi"],
    "Black": ["Cotton(lint)", "Urad", "Arhar/Tur", "Groundnut", "Onion", "Sesamum", "Linseed", "Safflower", "Rapeseed &Mustard", "Jute", "Bitter Gourd", "Drum Stick", "Jack Fruit", "Snak Guard", "Pump Kin", "Other Dry Fruit"],
    "Red": ["Arecanut", "Dry ginger", "Turmeric", "Gram", "Masoor", "Coriander", "Potato", "Soyabean", "Beans & Mutter(Vegetable)", "Bhindi", "Brinjal", "Citrus Fruit", "Cucumber", "Grapes", "Mango", "Orange", "Papaya", "Pome Fruit", "Tomato", "Cabbage", "Peas  (vegetable)", "Bottle Gourd", "Garlic", "Ginger", "Water Melon", "Colocosia", "Lentil", "Bean", "Jobster", "Perilla", "Rajmash Kholar", "Ricebean (nagadal)", "Ash Gourd", "Beet Root", "Lab-Lab", "Ribed Guard", "Yam"],
    "Clay": ["Other Kharif pulses", "Cashewnut", "Coconut", "Dry chillies", "other oilseeds", "Maize", "Moong(Green Gram)", "Sunflower", "Bajra", "Castor seed", "Horse-gram", "Jowar", "Korra", "Ragi", "Gram", "Sesamum", "Linseed", "Safflower", "other misc. pulses", "Samai", "Small millets", "Other  Rabi pulses", "Cauliflower", "Other Citrus Fruit"]
}



def make_data(State_Name, District_Name, Crop_Year, Season, Soil_Type, Area):
    Crops = crop_dict[Soil_Type]
