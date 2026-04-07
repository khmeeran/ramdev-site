import os
import json
import re

IMG_DIR = "aarimaterials_images"
OUTPUT_FILE = "products.json"

categories_map = {
    "Kundan Stones": r"kundan|stone|fitting|clip",
    "Beads & Pearls": r"bead|pearl|sugar|seed|bunch|wheat|drop|eye|tablet|loreal",
    "Threads & Zari": r"thread|zari|silk|nylon|cotton|dabka|zardosi|nakshi|kora",
    "Tools & Needles": r"needle|cutter|tape|glue|frame|stand|chalk|pencil|tool|screwdriver|winder",
    "Sequins & Patches": r"sequence|jamki|patch|chamki|paillette",
    "Jewelry Findings": r"charm|hook|clasp|pin|pendant|earring|bangle|bracelets|jewelry|jewellery"
}

products = []

# Get all files, filter out thumbnails (-150x150, -600x600, etc.)
if not os.path.exists(IMG_DIR):
    print(f"Error: {IMG_DIR} not found.")
    exit(1)

files = os.listdir(IMG_DIR)
# We prefer full versions (without size suffixes) and filter out non-image files
original_files = [f for f in files if not re.search(r'-\d+x\d+\.', f) and f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

# If there are NO original files, then maybe we should include some of those 600x600 ones as fallbacks
if not original_files:
    original_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

for filename in original_files:
    # Skip generic numbers or icons
    if re.match(r'^\d+\.(jpg|jpeg|png|webp)$', filename, re.IGNORECASE):
        continue
    if 'icon' in filename.lower() or 'logo' in filename.lower():
        continue
        
    # Basic cleaning of filename for title
    title = filename.replace("-", " ").replace("_", " ")
    title = re.sub(r'\.(jpg|jpeg|png|webp)$', '', title, flags=re.IGNORECASE)
    # Remove technical suffixes like "scaled"
    title = title.replace("scaled", "").strip()
    title = title.title()
    
    # Categorize
    category = "Other Materials"
    for cat_name, pattern in categories_map.items():
        if re.search(pattern, filename, re.IGNORECASE):
            category = cat_name
            break
            
    products.append({
        "title": title,
        "category": category,
        "image": f"{IMG_DIR}/{filename}",
        "price": "Wholesale"
    })

# Sort products to ensure categories are grouped nicely
products.sort(key=lambda x: (x['category'], x['title']))

with open(OUTPUT_FILE, "w") as f:
    json.dump(products, f, indent=4)

print(f"Generated {len(products)} products in {OUTPUT_FILE}")
