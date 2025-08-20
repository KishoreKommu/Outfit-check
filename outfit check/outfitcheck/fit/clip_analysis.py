import clip
import torch
from PIL import Image
from .color_palette import evaluate_color_palette
from .trend_model import evaluate_trend
from .segment import evaluate_fit

# Load the CLIP model once
model, preprocess = clip.load("ViT-B/32")
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

def rate_outfit_clip(image_path):
    # Load and preprocess image
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
    trend_labels = [
        "modern outfit", "outdated style", "stylish and trendy", "classic and elegant", 
        "casual", "formal", "streetwear", "vintage", "retro", "athleisure", "sporty", 
        "chic", "boho", "grunge", "minimalist", "eclectic", "high fashion", "business casual", 
        "punk", "preppy", "elegant", "sophisticated", "avant-garde", "urban", "cozy", 
        "bright colors", "monochrome", "layered style", "oversized", "skinny fit", 
        "loose fit", "bold prints", "pastels", "neon", "futuristic", "classic denim", 
        "floral print", "seasonal trends", "coordinated", "statement pieces", "textured fabric", 
        "color-blocking", "clean-cut", "structured", "luxe fabrics", "refined", "oversized accessories", 
        "casual chic", "casual chic", "street style", "bohemian", "traditional"
    ]
    text = clip.tokenize(trend_labels).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        similarity = (image_features @ text_features.T).softmax(dim=-1)

    # Get the best matching trend label and confidence
    top_score = similarity[0].argmax().item()
    label_confidence = similarity[0][top_score].item()
    trend_result = trend_labels[top_score]
    trend_reason = f"Detected as: **{trend_result}** outfit with confidence {label_confidence:.2f}."

    # Realistic dummy scores using other modules
    color_score, color_reason = evaluate_color_palette(image_path)
    fit_score, fit_reason = evaluate_fit(image_path)
    trend_score, _ = evaluate_trend(image_path)  # Optionally use real AI for trend scoring

    # Weight final score based on trend detection confidence
    weights = {
        "modern outfit": (1.1, 1.0, 1.0),
        "stylish and trendy": (1.0, 1.0, 1.2),
        "classic and elegant": (1.0, 1.2, 1.0),
        "outdated style": (1.0, 1.0, 0.8),
        # Add weightings for all other trend categories as necessary
    }

    trend_type = trend_result.lower().replace(" ", "_")
    weight_factors = weights.get(trend_type, (1.0, 1.0, 1.0))  # Default equal weighting
    w_color, w_fit, w_trend = weight_factors

    final_score = round((color_score * w_color + fit_score * w_fit + trend_score * w_trend) / (w_color + w_fit + w_trend), 1)

    # Enhanced suggestions based on detected trend type
    trend_suggestions = {
        "modern outfit": [
            "Add sleek accessories to accentuate the modern look.",
            "Opt for clean, tailored silhouettes to emphasize structure.",
            "Layer with a bold jacket or blazer for a refined touch."
        ],
        "streetwear": [
            "Pair with sneakers and a cool hoodie for the perfect street style.",
            "Add a graphic tee to stand out.",
            "Accessorize with a beanie or cap to complete the look."
        ],
        "bohemian": [
            "Flowy dresses or skirts are a great addition to this look.",
            "Add layered jewelry or a wide-brimmed hat.",
            "Earthy tones and natural fabrics complement boho style."
        ],
        "athleisure": [
            "Mix performance wear with street style for a sleek athleisure look.",
            "Pair with running shoes or high-top sneakers.",
            "Try bold, sporty prints for added flair."
        ],
        "vintage": [
            "Incorporate retro accessories, such as sunglasses or a vintage handbag.",
            "Go for high-waisted pants or skirts to capture the vintage essence.",
            "Use muted tones and classic patterns like polka dots or stripes."
        ],
        "punk": [
            "Pair with edgy accessories like studs, chains, or leather jackets.",
            "Combat boots or chunky shoes are ideal.",
            "Add statement prints and rough textures to the mix."
        ],
        # More trend-based suggestions...
    }

    suggestions = trend_suggestions.get(trend_result, [
        "Try layering with a jacket for a refined look.",
        "Pair it with neutral-toned shoes.",
        "Accessorize with minimal jewelry for style."
    ])

    return final_score, {
        "Color": color_reason,
        "Fit": fit_reason,
        "Trend": trend_reason
    }, suggestions[:3]
