import pandas as pd

# Read WooCommerce CSV file
woocommerce_df = pd.read_csv('woocommerce_products.csv')

# Create an empty list to store Shopify CSV rows
shopify_data = []

# Iterate over WooCommerce products and map fields to Shopify format
for _, row in woocommerce_df.iterrows():
    # Handle missing or NaN values in descriptions and other fields
    description = str(row['Description']) if pd.notnull(row['Description']) else ""
    short_description = str(row['Short description']) if pd.notnull(row['Short description']) else ""
    
    # Use Short description if Description is missing
    body_html = description if description else short_description
    
    # Handle missing or NaN values for numerical fields
    weight_kg = row['Weight (kg)'] if pd.notnull(row['Weight (kg)']) else 0
    sale_price = row['Sale price'] if pd.notnull(row['Sale price']) else ''
    regular_price = row['Regular price'] if pd.notnull(row['Regular price']) else ''
    stock_qty = row['Stock'] if pd.notnull(row['Stock']) else 0
    
    # Determine 'Published' as TRUE/FALSE based on the 'Published' column
    published_status = 'TRUE' if row['Published'] == 1 else 'FALSE'
    
    # Variant Inventory Policy
    inventory_policy = 'deny' if row['Backorders allowed?'] == 0 else 'continue'
    
    # Handle missing or NaN values for 'Images' (use default if missing)
    image_src = row['Images'] if pd.notnull(row['Images']) else ''
    
    # Create the Shopify row dictionary
    shopify_row = {
        'Handle': row['SKU'],  # Assuming SKU is unique and used as handle
        'Title': row['Name'],
        'Body (HTML)': body_html,
        'Vendor': row.get('Brands', ''),
        'Product Category': row['Categories'],
        'Tags': row['Tags'],
        'Published': published_status,
        'Option1 Name': 'Size',  # Example, assuming product variations based on size
        'Option1 Value': row['Attribute 1 value(s)'],  # Example mapping for variations
        'Variant SKU': row['SKU'],
        'Variant Grams': weight_kg * 1000,  # Convert kg to grams
        'Variant Inventory Tracker': 'shopify',
        'Variant Inventory Qty': stock_qty,
        'Variant Inventory Policy': inventory_policy,
        'Variant Fulfillment Service': 'manual',
        'Variant Price': sale_price,
        'Variant Compare At Price': regular_price,
        'Variant Requires Shipping': 'TRUE',
        'Variant Taxable': 'TRUE' if row['Tax status'] == 'taxable' else 'FALSE',
        'Variant Barcode': '',  # If you have barcode data, map it here
        'Image Src': image_src,  # Assuming one image URL per product
        'Image Position': 1,
        'Image Alt Text': row['Name'],  # Could use Name or Description as alt text
        'Gift Card': 'FALSE',
        'SEO Title': row['Name'],
        'SEO Description': description[:320] if description else short_description[:320],  # Slice to 320 chars
        'Google Shopping / Google Product Category': row['Categories'],
        'Google Shopping / Gender': 'Unisex',  # Example, adjust as per your data
        'Google Shopping / Age Group': 'Adult',  # Example, adjust as per your data
        'Status': 'active' if row['Published'] == 1 else 'draft'
    }
    
    # Append the mapped row to shopify_data
    shopify_data.append(shopify_row)

# Convert the list of dictionaries to a DataFrame and save as CSV
shopify_df = pd.DataFrame(shopify_data)
shopify_df.to_csv('shopify_products.csv', index=False)
