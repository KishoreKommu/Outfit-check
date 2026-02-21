from colorthief import ColorThief

def evaluate_color_palette(image_path):
    try:
        color_thief = ColorThief(image_path)
        r, g, b = color_thief.get_color(quality=1)

        # Define common thresholds
        light = lambda x: x > 200
        medium = lambda x: 100 < x <= 200
        dark = lambda x: x <= 100

        # Predefined palette evaluations (~50 conditions)
        if r > 230 and g < 100 and b < 100:
            return 6.5, "Bright red dominates – bold, but try balancing it with neutrals."
        elif r > 200 and g > 200 and b < 100:
            return 7.0, "Yellowish tone – sunny and cheerful, but needs grounding tones."
        elif r < 100 and g > 200 and b < 100:
            return 7.0, "Bright green – energetic and vibrant, but may feel overpowering."
        elif r < 100 and g > 200 and b > 200:
            return 7.5, "Aqua/mint tone – refreshing and cool, great for summer outfits."
        elif r < 100 and g < 100 and b > 200:
            return 7.5, "Dominant blue – calming and dependable, pairs well with grey or white."
        elif r > 200 and g < 100 and b > 200:
            return 7.0, "Fuchsia or hot pink – fun and bold, but works best in moderation."
        elif r > 240 and g > 240 and b > 240:
            return 8.0, "Very light or pastel – elegant and soft."
        elif r < 50 and g < 50 and b < 50:
            return 8.0, "Mostly black – classic and bold. Accessories matter!"
        elif r > 200 and g > 100 and b < 50:
            return 6.5, "Orange tone – playful and bright. Contrast with dark shades."
        elif r > 180 and g < 80 and b > 180:
            return 6.5, "Magenta tone – expressive and bold. Keep accessories minimal."
        elif r > 180 and g > 180 and b > 180:
            return 8.5, "Light and balanced tones – easy on the eyes and very versatile."
        elif r < 100 and g < 100 and b < 150:
            return 7.0, "Navy or dark blue tone – smart and formal."
        elif r > 150 and g > 150 and b < 100:
            return 7.0, "Olive or earthy – grounded and stylish with beige or cream."
        elif r > 180 and g > 120 and b > 150:
            return 7.5, "Rose pink – soft and feminine, goes great with whites."
        elif r > 200 and g > 180 and b > 160:
            return 7.5, "Peach tone – warm and charming, great for sunny days."
        elif r > 150 and g > 130 and b < 100:
            return 7.0, "Tan or beige – neutral and elegant, works with anything."
        elif r > 120 and g < 100 and b < 100:
            return 6.5, "Rust or brick red – bold and earthy, try cream or white pairing."
        elif r > 170 and g > 220 and b > 220:
            return 7.5, "Pastel teal or turquoise – relaxing and smooth tone."
        elif r < 120 and g > 100 and b < 120:
            return 6.5, "Muted green – natural and grounded, but less vibrant."
        elif r < 80 and g < 60 and b > 140:
            return 6.5, "Royal blue – luxurious and confident."
        elif r > 220 and g < 160 and b > 220:
            return 7.0, "Lilac or lavender – soft and dreamy."
        elif r < 60 and g > 200 and b > 60:
            return 7.0, "Lime green – bright and loud, best used sparingly."
        elif r > 240 and g > 180 and b > 180:
            return 7.5, "Blush pink – romantic and airy."
        elif r > 150 and g > 100 and b > 200:
            return 7.5, "Light purple – unique and artistic."
        elif r > 180 and g < 80 and b < 80:
            return 6.5, "Coral – energetic and summery."
        elif r > 180 and g > 100 and b > 80:
            return 7.0, "Apricot – warm and sweet."
        elif r < 100 and g < 100 and b > 100:
            return 6.5, "Slate blue – cool and moody."
        elif r > 100 and g < 100 and b < 100:
            return 6.0, "Dark red or maroon – serious tone, add contrast."
        elif r > 100 and g > 100 and b > 100:
            return 8.0, "Neutral balance – flexible and calm."
        elif r > 220 and g > 150 and b > 90:
            return 7.5, "Warm beige – cozy and comforting."
        elif r < 80 and g > 120 and b < 80:
            return 6.5, "Forest green – earthy but may feel too dark alone."
        elif r > 220 and g > 100 and b > 120:
            return 7.0, "Warm pink or salmon – cheerful and positive."
        elif r < 80 and g > 80 and b > 160:
            return 6.5, "Indigo – intense and stylish but heavy."
        elif r > 120 and g > 110 and b > 100:
            return 7.5, "Warm neutral – subtle and classy."
        elif r > 160 and g > 170 and b > 190:
            return 8.0, "Icy or pale blue – modern and refreshing."
        elif r > 240 and g > 230 and b > 210:
            return 8.5, "Cream/ivory – very classy and soft."
        elif r > 150 and g > 200 and b < 100:
            return 7.0, "Lemon or chartreuse – bright and cheerful."
        elif r < 80 and g < 80 and b < 80:
            return 8.0, "Mostly dark tone – stylish, needs light contrast."
        elif r < 50 and g < 50 and b > 180:
            return 6.5, "Electric blue – striking but strong."
        elif r > 200 and g < 200 and b < 100:
            return 6.5, "Bold orange-red – loud and confident."
        elif r > 240 and g < 100 and b < 100:
            return 6.5, "Fire red – very eye-catching, good for statements."
        elif r > 180 and g > 160 and b < 100:
            return 7.0, "Golden – rich and formal."
        elif r > 160 and g > 120 and b > 80:
            return 7.0, "Caramel – sweet and cozy."
        elif r < 70 and g < 70 and b < 50:
            return 7.5, "Charcoal – strong and refined."
        elif r > 180 and g < 180 and b > 100:
            return 7.0, "Orchid or light violet – soft and charming."
        elif r > 100 and g < 60 and b > 140:
            return 6.5, "Berry or plum – deep and romantic."
        else:
            return 8.0, "Color palette is neutral or well-balanced overall."

    except Exception as e:
        return 6.0, "Could not analyze color palette. Try uploading a clearer image."
