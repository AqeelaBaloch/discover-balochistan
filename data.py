
# ==========================================
# DISCOVER BALOCHISTAN - DESTINATION DATABASE
# ==========================================

DESTINATIONS = [
    {
        "id": 1,
        "name": "Hingol National Park",
        "region": "Lasbela",
        "category": "Nature",
        "interests": ["nature", "adventure", "wildlife"],
        "description": (
            "Hingol National Park is known for its dramatic rock formations, "
            "mountains, natural landscapes and coastal scenery."
        ),
        "roman_description": (
            "Hingol National Park apni khoobsurat chattanon, paharon, "
            "qudrati manazir aur sahili khubsurti ke liye mashhoor hai."
        ),
        "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=900",
        "note": "Check local access, weather and travel guidance before visiting."
    },
    {
        "id": 2,
        "name": "Kund Malir Beach",
        "region": "Lasbela",
        "category": "Beach",
        "interests": ["beach", "nature", "relaxation"],
        "description": (
            "Kund Malir is a scenic beach located along the Makran "
            "Coastal Highway in Balochistan."
        ),
        "roman_description": (
            "Kund Malir Balochistan ka ek khoobsurat sahili maqam hai. "
            "Yeh Makran Coastal Highway ke qareeb waqay hai."
        ),
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=900",
        "note": "Check sea conditions and local travel advisories."
    },
    {
        "id": 3,
        "name": "Ziarat",
        "region": "Ziarat",
        "category": "Mountains & History",
        "interests": ["mountains", "history", "nature"],
        "description": (
            "Ziarat is a hill station famous for its ancient juniper "
            "forests and the historic Quaid-e-Azam Residency."
        ),
        "roman_description": (
            "Ziarat Balochistan ka mashhoor pahari maqam hai. "
            "Yeh apne purane juniper ke darakhton aur tareekhi "
            "Quaid-e-Azam Residency ki wajah se mashhoor hai."
        ),
        "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=900",
        "note": "Check seasonal weather and road conditions."
    },
    {
        "id": 4,
        "name": "Hanna Lake",
        "region": "Quetta",
        "category": "Lake & Nature",
        "interests": ["nature", "relaxation"],
        "description": (
            "Hanna Lake is a well-known lake and recreational "
            "destination near Quetta."
        ),
        "roman_description": (
            "Hanna Lake Quetta ke qareeb ek mashhoor jheel aur "
            "tafreehi maqam hai. Yahan qudrati manazir dekhe ja sakte hain."
        ),
        "image": "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?w=900",
        "note": "Confirm current lake conditions and facilities locally."
    },
    {
        "id": 5,
        "name": "Gwadar",
        "region": "Gwadar",
        "category": "Coastal",
        "interests": ["beach", "nature", "culture"],
        "description": (
            "Gwadar is a coastal city in Balochistan known for "
            "its beaches, viewpoints and maritime scenery."
        ),
        "roman_description": (
            "Gwadar Balochistan ka ek sahili shehar hai. "
            "Yeh apne samandari manazir, sahilon aur viewpoints "
            "ke liye jana jata hai."
        ),
        "image": "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=900",
        "note": "Check current travel advisories and local access information."
    },
    {
        "id": 6,
        "name": "Moola Chotok",
        "region": "Khuzdar",
        "category": "Waterfalls & Nature",
        "interests": ["nature", "adventure", "waterfalls", "mountains"],
        "description": (
            "Moola Chotok is a natural ravine in Khuzdar District, "
            "Balochistan. It is known for waterfalls, rocky cliffs, "
            "streams and natural pools. The route includes rough "
            "off-road sections."
        ),
        "roman_description": (
            "Moola Chotok Khuzdar, Balochistan mein waqay ek khoobsurat "
            "qudrati wadi hai. Yeh waterfalls, buland chattanon, "
            "pani ke chashmon aur qudrati pools ke liye mashhoor hai. "
            "Yahan pohanchne ka rasta mushkil ho sakta hai."
        ),
        "image": "https://images.unsplash.com/photo-1432405972618-c60b0225b8f9?w=900",
        "note": (
            "Confirm local access, weather, road conditions and "
            "transport arrangements with experienced local guides."
        )
    }
]


# ==========================================
# CHATBOT - ENGLISH AND ROMAN URDU
# ==========================================

def chatbot_reply(message, language="en"):

    q = message.lower()

    destination_keywords = {
        "ziarat": ["ziarat", "juniper", "residency", "jinnah"],
        "hingol": ["hingol"],
        "kund": ["kund malir", "kund", "malir"],
        "hanna": ["hanna lake", "hanna"],
        "gwadar": ["gwadar"],
        "moola": [
            "moola chotok",
            "moola chutok",
            "moola",
            "chotok",
            "chutok"
        ]
    }

    responses = {
        "ziarat": {
            "en": (
                "Ziarat is a famous hill station in Balochistan. "
                "It is known for its ancient juniper forests and the "
                "historic Quaid-e-Azam Residency. Visitors can enjoy "
                "mountain scenery and explore the natural environment. "
                "Check weather and road conditions before travelling."
            ),
            "ur": (
                "Ziarat Balochistan ka ek mashhoor pahari maqam hai. "
                "Yeh apne purane juniper ke darakhton aur tareekhi "
                "Quaid-e-Azam Residency ke liye mashhoor hai. "
                "Yahan aap paharon ke khoobsurat manazir dekh sakte hain. "
                "Safar se pehle mausam aur sarkon ki surat-e-haal check karein."
            )
        },

        "hingol": {
            "en": (
                "Hingol National Park is known for its mountains, "
                "unusual rock formations and natural coastal landscapes. "
                "It is a destination for nature and adventure lovers. "
                "Check local access and travel guidance before visiting."
            ),
            "ur": (
                "Hingol National Park apne khoobsurat paharon, "
                "ajeeb-o-ghareeb chattanon aur qudrati sahili manazir "
                "ke liye mashhoor hai. Yeh nature aur adventure pasand "
                "karne walon ke liye ek dilchasp maqam hai."
            )
        },

        "kund": {
            "en": (
                "Kund Malir is a scenic beach along the Makran "
                "Coastal Highway. Visitors can enjoy coastal views "
                "and natural beauty. Check sea conditions and local "
                "travel advisories before your trip."
            ),
            "ur": (
                "Kund Malir Makran Coastal Highway ke qareeb ek "
                "khoobsurat beach hai. Yahan samandar ke dilkash "
                "manazir aur qudrati khubsurti dekhi ja sakti hai. "
                "Safar se pehle samandar ki halat aur local travel "
                "advisories check karein."
            )
        },

        "hanna": {
            "en": (
                "Hanna Lake is a well-known recreational destination "
                "near Quetta. It is popular for its lake scenery "
                "and natural surroundings. Check current lake conditions "
                "and available facilities before visiting."
            ),
            "ur": (
                "Hanna Lake Quetta ke qareeb ek mashhoor tafreehi "
                "maqam hai. Yeh apni jheel aur qudrati manazir "
                "ke liye jana jata hai. Jane se pehle jheel ki "
                "maujooda halat aur sahuliyat maloom karein."
            )
        },

        "gwadar": {
            "en": (
                "Gwadar is a coastal city in Balochistan. "
                "It is known for its beaches, viewpoints and "
                "beautiful maritime scenery. Check current travel "
                "advisories before planning your visit."
            ),
            "ur": (
                "Gwadar Balochistan ka ek sahili shehar hai. "
                "Yeh apne beaches, viewpoints aur samandari "
                "manazir ke liye mashhoor hai. Jane se pehle "
                "maujooda travel advisories check karein."
            )
        },

        "moola": {
            "en": (
                "Moola Chotok is a natural ravine in Khuzdar District, "
                "Balochistan. It is famous for its waterfalls, rocky "
                "cliffs, streams and natural pools. The route is remote "
                "and rough, so an experienced local driver and suitable "
                "4x4 transport may be needed. Confirm current access "
                "and weather conditions before travelling."
            ),
            "ur": (
                "Moola Chotok Khuzdar District, Balochistan mein "
                "waqay ek khoobsurat qudrati wadi hai. Yeh apne "
                "waterfalls, buland chattanon, pani ke chashmon aur "
                "qudrati pools ke liye mashhoor hai. Yahan ka rasta "
                "mushkil aur door daraz ho sakta hai. Is liye safar "
                "se pehle local guide, transport aur mausam ki "
                "surat-e-haal maloom karein."
            )
        }
    }

    selected_destination = None

    for destination, keywords in destination_keywords.items():

        if any(keyword in q for keyword in keywords):
            selected_destination = destination
            break

    lang = "ur" if language == "ur" else "en"

    if selected_destination:
        return responses[selected_destination][lang]

    if lang == "ur":
        return (
            "Main Balochistan ke tourism ke bare mein maloomat de sakta hoon. "
            "Aap Ziarat, Hingol National Park, Kund Malir, Hanna Lake, "
            "Gwadar ya Moola Chotok ke bare mein pooch sakte hain."
        )

    return (
        "I can provide information about tourism in Balochistan. "
        "You can ask me about Ziarat, Hingol National Park, "
        "Kund Malir, Hanna Lake, Gwadar or Moola Chotok."
    )


# ==========================================
# PERSONALIZED DESTINATION RECOMMENDATIONS
# ==========================================

def recommend_destinations(interests):

    selected = {str(x).lower() for x in interests}

    ranked = []

    for place in DESTINATIONS:

        score = len(selected.intersection(place["interests"]))

        if score:
            ranked.append((score, place))

    ranked.sort(key=lambda x: x[0], reverse=True)

    return [place for _, place in ranked] or DESTINATIONS[:3]


# ==========================================
# BILINGUAL SMART TRIP PLANNER
# ==========================================

def build_itinerary(destination, days, interests, language="en"):

    place = next(
        (
            p for p in DESTINATIONS
            if p["name"].lower() == str(destination).lower()
        ),
        None
    )

    if not place:
        error = (
            "Please choose a destination from the list."
            if language == "en"
            else "Barah-e-karam list mein se tourist maqam select karein."
        )
        return {"error": error}

    interest_text = (
        ", ".join(interests)
        if interests
        else place["category"].lower()
    )

    if language == "ur":

        activities = [
            f"Day 1: {place['name']} explore karein aur is maqam ke bare mein maloomat hasil karein.",
            f"Day 2: {interest_text} se related activities ka lutf uthayein.",
            "Day 3: Local travel conditions check karne ke baad qareebi maqamat explore karein.",
            "Day 4: Photography karein aur qudrati manazir ka lutf uthayein.",
            "Day 5: Local culture aur environment ke bare mein janein.",
            "Day 6: Apni dilchaspi ke mutabiq mazeed activities karein.",
            "Day 7: Apne safar ko mukammal karein aur wapsi ki tayari karein."
        ]

        disclaimer = (
            "Yeh sirf ek sample itinerary hai. Safar se pehle "
            "routes, timings, costs, weather aur safety information "
            "local sources se confirm karein."
        )

    else:

        activities = [
            f"Day 1: Explore {place['name']} and learn about the area.",
            f"Day 2: Enjoy activities related to {interest_text}.",
            "Day 3: Explore nearby attractions after checking local travel conditions.",
            "Day 4: Enjoy photography and explore the natural surroundings.",
            "Day 5: Learn about the local culture and environment.",
            "Day 6: Enjoy additional activities based on your interests.",
            "Day 7: Complete your trip and prepare for departure."
        ]

        disclaimer = (
            "Sample itinerary only. Confirm routes, opening times, "
            "costs, weather and safety information locally."
        )

    return {
        "destination": place["name"],
        "days": activities[:days],
        "disclaimer": disclaimer
    }
