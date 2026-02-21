import random

# --- Evaluate Color Palette ---
def evaluate_color_palette(image_path):
    score = round(random.uniform(6.0, 9.0), 1)
    reasons = [
        "Great contrast and complementary tones.",
        "Colors slightly clash; try more neutral combos.",
        "Excellent seasonal color choice.",
        "Overuse of bright tones; consider balancing with soft shades.",
        "Muted tones give a classy and elegant appearance.",
        "Bold primary colors convey confidence.",
        "Pastel shades work beautifully with your complexion.",
        "Color choice suits current fashion trends.",
        "Too many warm tones; try mixing with cool shades.",
        "Color blocking adds a trendy edge.",
        "Too monotone; add a pop of color.",
        "Well-matched upper and lower pieces.",
        "Prints are vibrant and well-balanced.",
        "Off-tones disrupt the flow of the outfit.",
        "Neutrals are safe but could use contrast.",
        "Bright colors stand out and draw attention.",
        "Earthy tones give a grounded and mature vibe.",
        "Slight mismatch between accessories and outfit tones.",
        "Color choice highlights your personality.",
        "Smart use of accent colors to break uniformity.",
    ]
    return score, random.choice(reasons)

# --- Evaluate Fit ---
def evaluate_fit(image_path):
    score = round(random.uniform(5.5, 9.5), 1)
    reasons = [
        "Outfit fits well and accentuates your body shape.",
        "Top seems too loose; a better fit could improve the look.",
        "Pants are too baggy; try a tapered fit.",
        "Perfectly tailored for your body type.",
        "Slight bulge near midsection—try a better cut.",
        "Sleeves fit well, but overall body looks tight.",
        "Smart silhouette from shoulders to ankles.",
        "Jacket too long—shorter cuts might help.",
        "Relaxed fit adds a casual, comfy vibe.",
        "Outfit enhances posture and body symmetry.",
        "Shoulder seams sit perfectly, indicating good fit.",
        "Poor hemline affects the outfit flow.",
        "Shirt length is ideal; not too long or short.",
        "Cuffs are oversized—try a slimmer wrist finish.",
        "Tight neckline disrupts comfort and flow.",
        "Waistline fit is spot-on for body proportions.",
        "Baggy pants drag the look down—tapered would lift it.",
        "Slight shoulder drop gives streetwear appeal.",
        "Bottoms balance the top perfectly.",
        "Outfit shape suits athletic body types well.",
    ]
    return score, random.choice(reasons)

# --- Evaluate Trend Relevance ---
def evaluate_trend(image_path):
    score = round(random.uniform(5.0, 9.0), 1)
    reasons = [
        "Modern and in-trend look.",
        "Shoes seem outdated compared to the rest of the outfit.",
        "Mix of retro and modern style, well balanced.",
        "Overall look is classic but needs a trendy twist.",
        "Outfit aligns with latest fashion aesthetics.",
        "Print style is outdated—try minimalist patterns.",
        "Accessories add trend relevance.",
        "Use of textures makes outfit look premium.",
        "Monochrome style is back and works well here.",
        "Cropped style adds an edgy twist.",
        "Denim-on-denim is a bold trend and pulled off well.",
        "Layering follows modern fashion logic.",
        "Certain pieces feel a bit last-season.",
        "Outfit looks inspired by celebrity trends.",
        "Pockets and zips reflect utilitarian trend.",
        "Footwear choice elevates the trendiness.",
        "Flared cuts are trending and fit nicely here.",
        "Outfit needs an upgrade to align with Gen-Z styles.",
        "Old-school elements give retro aesthetic appeal.",
        "Color palette supports current fashion movements.",
    ]
    return score, random.choice(reasons)

# --- Style Suggestions (random 3 picked) ---
def get_style_suggestions(color_score, fit_score, trend_score):
    suggestions = [
        "Try pairing your outfit with minimalist white sneakers.",
        "Use a belt to define your waistline better.",
        "Layer with a jacket or shrug for added depth.",
        "Add subtle accessories like a chain or a watch.",
        "Swap your top for a neutral shade for better contrast.",
        "Incorporate textures like leather or denim for dimension.",
        "Try ankle-length pants to enhance proportions.",
        "Experiment with oversized fits for a street-style edge.",
        "Add a pop color bag or clutch to elevate style.",
        "Choose fitted cuffs to create cleaner sleeve lines.",
        "Go for high-rise bottoms for a more structured look.",
        "Switch to muted shades for a minimalist aesthetic.",
        "Roll up sleeves for a casual, confident look.",
        "Contrast shoes or socks can make your look stand out.",
        "Try layering with patterns like stripes or plaid.",
        "Incorporate a statement piece like a scarf or cap.",
    ]
    return random.sample(suggestions, k=3)

# --- Final Rating Logic ---
def rate_outfit(image_path="dummy.jpg"):
    color_score, color_reason = evaluate_color_palette(image_path)
    fit_score, fit_reason = evaluate_fit(image_path)
    trend_score, trend_reason = evaluate_trend(image_path)

    final_score = round((color_score + fit_score + trend_score) / 3, 1)

    reasons = {
        "Color": color_reason,
        "Fit": fit_reason,
        "Trend": trend_reason,
    }

    suggestions = get_style_suggestions(color_score, fit_score, trend_score)

    return final_score, reasons, suggestions
