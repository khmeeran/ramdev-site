import json

# Read the full products list
with open('products.json', 'r') as f:
    products = json.load(f)

# Hardcode the data into the HTML template to bypass local CORS issues
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wholesale Catalogue | Ramdev Lace House</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #1a237e;
            --accent: #E91E63;
            --whatsapp: #25D366;
            --text-main: #333;
            --text-muted: #777;
            --border: #eeeeee;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: #ffffff;
            color: var(--text-main);
            line-height: 1.5;
        }}

        .top-bar {{ background: #f8f8f8; border-bottom: 1px solid var(--border); padding: 8px 0; font-size: 0.75rem; color: var(--text-muted); }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 0 20px; }}
        .top-content {{ display: flex; justify-content: space-between; align-items: center; }}

        header {{ padding: 20px 0; border-bottom: 1px solid var(--border); background: white; position: sticky; top: 0; z-index: 1000; }}
        .header-main {{ display: flex; justify-content: space-between; align-items: center; gap: 20px; }}
        .logo {{ font-size: 1.8rem; font-weight: 800; color: var(--primary); text-decoration: none; letter-spacing: -1px; flex-shrink: 0; }}
        
        .search-container {{ flex-grow: 1; max-width: 600px; position: relative; }}
        .search-container input {{
            width: 100%; padding: 12px 20px; border: 2px solid #eee; border-radius: 8px;
            outline: none; font-size: 0.9rem; transition: border-color 0.3s;
        }}
        .search-container input:focus {{ border-color: var(--primary); }}

        .shop-container {{ display: grid; grid-template-columns: 260px 1fr; gap: 40px; padding: 40px 0; }}

        .sidebar-title {{ font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px; border-bottom: 2px solid var(--primary); display: inline-block; padding-bottom: 5px; }}
        .category-list {{ list-style: none; }}
        .category-item {{ padding: 10px 0; border-bottom: 1px solid #f0f0f0; cursor: pointer; font-size: 0.9rem; color: #555; transition: all 0.2s; display: flex; justify-content: space-between; }}
        .category-item:hover, .category-item.active {{ color: var(--accent); font-weight: 600; padding-left: 5px; }}
        .category-count {{ color: #bbb; font-size: 0.75rem; font-weight: 400; }}

        .grid-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }}
        .product-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 25px; }}
        
        .product-card {{ border: 1px solid #f0f0f0; padding: 15px; transition: all 0.3s; display: flex; flex-direction: column; border-radius: 8px; }}
        .product-card:hover {{ border-color: #ddd; box-shadow: 0 10px 25px rgba(0,0,0,0.05); transform: translateY(-5px); }}
        
        .img-box {{ width: 100%; aspect-ratio: 1; background: #fdfdfd; border-radius: 4px; overflow: hidden; margin-bottom: 15px; border: 1px solid #fafafa; }}
        .img-box img {{ width: 100%; height: 100%; object-fit: cover; }}

        .p-info {{ flex-grow: 1; text-align: center; }}
        .p-cat {{ font-size: 0.65rem; color: var(--accent); text-transform: uppercase; font-weight: 700; margin-bottom: 8px; display: block; letter-spacing: 0.5px; }}
        .p-title {{ font-size: 0.85rem; font-weight: 600; color: #333; margin-bottom: 12px; min-height: 2.5em; overflow: hidden; }}
        .p-price {{ font-weight: 700; color: var(--primary); font-size: 1rem; margin-bottom: 15px; display: block; }}

        .btn-order {{ 
            width: 100%; padding: 12px; background: #f8f8f8; border: 1px solid #ddd; 
            color: #444; font-size: 0.7rem; font-weight: 700; text-transform: uppercase;
            cursor: pointer; transition: all 0.3s; border-radius: 6px; display: flex; align-items: center; justify-content: center; gap: 8px;
        }}
        .product-card:hover .btn-order {{ background: var(--whatsapp); border-color: var(--whatsapp); color: white; }}

        .load-more {{ text-align: center; margin-top: 60px; }}
        .btn-load {{ padding: 16px 50px; background: var(--primary); color: white; border: none; font-weight: 700; text-transform: uppercase; cursor: pointer; border-radius: 8px; font-size: 0.85rem; box-shadow: 0 4px 15px rgba(26, 35, 126, 0.2); transition: all 0.3s; }}
        .btn-load:hover {{ background: #0d1440; transform: scale(1.02); }}

        footer {{ background: #111; color: #888; padding: 60px 0 30px; margin-top: 80px; }}
        .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; }}
        .footer-title {{ color: white; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; margin-bottom: 20px; }}
        
        @media (max-width: 768px) {{
            .shop-container {{ grid-template-columns: 1fr; }}
            .sidebar {{ display: none; }}
            .header-main {{ flex-direction: column; align-items: flex-start; }}
            .search-container {{ max-width: 100%; }}
        }}
    </style>
</head>
<body>

    <div class="top-bar">
        <div class="container top-content">
            <div>Premium Wholesale Embroidery Materials</div>
            <div>WhatsApp: +91 99626 43165 | GST: 33ARZPR4322G1Z9</div>
        </div>
    </div>

    <header>
        <div class="container header-main">
            <a href="index.html" class="logo">RAMDEV</a>
            <div class="search-container">
                <input type="text" id="searchInput" placeholder="Search 1,700+ materials...">
            </div>
            <div style="display: flex; gap: 20px; font-size: 0.75rem; font-weight: 700;">
                <a href="index.html" style="text-decoration: none; color: inherit;">HOME</a>
                <a href="tel:+919962643165" style="text-decoration: none; color: var(--accent);">CALL US</a>
            </div>
        </div>
    </header>

    <main class="container shop-container">
        <aside class="sidebar">
            <h3 class="sidebar-title">Collections</h3>
            <ul class="category-list" id="categoryList"></ul>

            <div style="margin-top: 50px; padding: 20px; background: #fff5f8; border-radius: 12px; border: 1px solid #ffe4e9;">
                <h4 style="font-size: 0.8rem; color: var(--accent); margin-bottom: 10px;">Bulk Inquiry</h4>
                <p style="font-size: 0.75rem; color: #666; line-height: 1.6;">For volume orders and customized boutique supplies, please contact our support.</p>
                <a href="https://wa.me/919962643165" style="display: inline-block; margin-top: 15px; color: var(--whatsapp); font-weight: 700; text-decoration: none; font-size: 0.8rem;">WhatsApp Support →</a>
            </div>
        </aside>

        <section class="content">
            <div class="grid-header">
                <h2 id="gridTitle" style="font-size: 1.4rem;">All Materials</h2>
                <div style="font-size: 0.8rem; color: #999; font-weight: 500;">Found <span id="resultCount">0</span> items</div>
            </div>

            <div class="product-grid" id="productGrid"></div>

            <div class="load-more" id="loadMoreContainer">
                <button class="btn-load" id="loadMoreBtn">Load More Materials</button>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3 class="footer-title">Ramdev Lace House</h3>
                    <p style="font-size: 0.8rem; line-height: 1.8;">Leading wholesaler since 2011. Providing high-quality Aari work materials, beads, stones, and tailoring supplies to boutiques across India.</p>
                </div>
                <div>
                    <h3 class="footer-title">Quick Links</h3>
                    <ul style="list-style: none; font-size: 0.8rem; line-height: 2;">
                        <li>Home</li>
                        <li>About Us</li>
                        <li>Contact</li>
                        <li>Wholesale Terms</li>
                    </ul>
                </div>
                <div>
                    <h3 class="footer-title">Location</h3>
                    <p style="font-size: 0.8rem; line-height: 1.8;">No. 70, Vembuli Amman Kovil Street,<br>Tiruvallur, Tamil Nadu 602001</p>
                </div>
            </div>
            <div style="margin-top: 50px; padding-top: 20px; border-top: 1px solid #222; text-align: center; font-size: 0.7rem; color: #555;">
                © 2026 RAMDEV LACE HOUSE. ALL RIGHTS RESERVED.
            </div>
        </div>
    </footer>

    <script>
        const allProducts = {json.dumps(products)};
        let displayedCount = 24;
        let currentFilter = 'All';
        let searchQuery = '';

        function renderCategories() {{
            const counts = allProducts.reduce((acc, p) => {{
                acc[p.category] = (acc[p.category] || 0) + 1;
                return acc;
            }}, {{}});

            const categories = ['All', ...Object.keys(counts).sort()];
            const list = document.getElementById('categoryList');
            list.innerHTML = '';
            
            categories.forEach(cat => {{
                const li = document.createElement('li');
                li.className = `category-item ${{cat === currentFilter ? 'active' : ''}}`;
                li.innerHTML = `
                    <span>${{cat === 'All' ? 'Full Collection' : cat}}</span>
                    <span class="category-count">(${{cat === 'All' ? allProducts.length : counts[cat]}})</span>
                `;
                li.onclick = () => {{
                    currentFilter = cat;
                    displayedCount = 24;
                    document.getElementById('gridTitle').textContent = cat === 'All' ? 'All Materials' : cat;
                    renderCategories();
                    renderProducts();
                }};
                list.appendChild(li);
            }});
        }}

        function renderProducts() {{
            const grid = document.getElementById('productGrid');
            const loadMoreBtn = document.getElementById('loadMoreContainer');
            
            const filtered = allProducts.filter(p => {{
                const matchCat = currentFilter === 'All' || p.category === currentFilter;
                const matchSearch = p.title.toLowerCase().includes(searchQuery);
                return matchCat && matchSearch;
            }});

            document.getElementById('resultCount').textContent = filtered.length;
            
            const toDisplay = filtered.slice(0, displayedCount);
            grid.innerHTML = toDisplay.map(p => `
                <div class="product-card">
                    <div class="img-box">
                        <img src="${{p.image}}" alt="${{p.title}}" loading="lazy">
                    </div>
                    <div class="p-info">
                        <span class="p-cat">${{p.category}}</span>
                        <h3 class="p-title">${{p.title}}</h3>
                        <span class="p-price">Wholesale</span>
                        <button class="btn-order" onclick="window.location.href='https://wa.me/919962643165?text=I am interested in: ${{encodeURIComponent(p.title)}}'">
                            <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
                            Order via WhatsApp
                        </button>
                    </div>
                </div>
            `).join('');

            loadMoreBtn.style.display = displayedCount >= filtered.length ? 'none' : 'block';
        }}

        document.getElementById('searchInput').addEventListener('input', (e) => {{
            searchQuery = e.target.value.toLowerCase();
            displayedCount = 24;
            renderProducts();
        }});

        document.getElementById('loadMoreBtn').addEventListener('click', () => {{
            displayedCount += 24;
            renderProducts();
        }});

        renderCategories();
        renderProducts();
    </script>
</body>
</html>"""

with open('catalogue.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Catalogue fixed and data embedded.")
