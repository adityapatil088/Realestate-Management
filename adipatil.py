import tkinter as tk
from tkinter import messagebox, simpledialog

# Sample real estate data
properties = [
    {"id": 1, "type": "House", "bedrooms": 4, "bathrooms": 3, "price": 250000, "image": "house1.jpg"},
    {"id": 2, "type": "Apartment", "bedrooms": 2, "bathrooms": 1, "price": 120000, "image": "apt1.jpg"},
    {"id": 3, "type": "House", "bedrooms": 3, "bathrooms": 2, "price": 180000, "image": "house2.jpg"},
    {"id": 4, "type": "Condo", "bedrooms": 1, "bathrooms": 1, "price": 90000, "image": "condo1.jpg"},
    # Add more property details as needed
]

def show_properties():
    property_frame.pack_forget()
    property_frame.pack()
    for prop in properties:
        property_text = f"ID: {prop['id']}, Type: {prop['type']}, Bedrooms: {prop['bedrooms']}, Bathrooms: {prop['bathrooms']}, Price: ${prop['price']}"
        label = tk.Label(property_frame, text=property_text, bg="lightblue")
        label.bind("<Button-1>", lambda event, prop=prop: show_property_details(prop))
        label.pack()

def show_property_details(property):
    details_window = tk.Toplevel(root)
    details_window.title("Property Details")
    property_text = f"Type: {property['type']}\nBedrooms: {property['bedrooms']}\nBathrooms: {property['bathrooms']}\nPrice: ${property['price']}"
    property_label = tk.Label(details_window, text=property_text)
    property_label.pack()

def add_property():
    new_id = len(properties) + 1
    prop_type = simpledialog.askstring("Property Type", "Enter property type:")
    bedrooms = simpledialog.askinteger("Bedrooms", "Enter number of bedrooms:")
    bathrooms = simpledialog.askinteger("Bathrooms", "Enter number of bathrooms:")
    price = simpledialog.askfloat("Price", "Enter price:")
    
    new_property = {
        "id": new_id,
        "type": prop_type,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "price": price,
        "image": "default_image.jpg"
    }
    properties.append(new_property)
    messagebox.showinfo("Added", "Property added! Refresh property list to view.")
    refresh_properties()

def delete_property():
    property_id = simpledialog.askinteger("Delete Property", "Enter Property ID to delete:")
    if property_id is not None:
        for prop in properties:
            if prop["id"] == property_id:
                properties.remove(prop)
                messagebox.showinfo("Deleted", f"Property with ID {property_id} deleted!")
                refresh_properties()
                return
        messagebox.showinfo("Not Found", f"No property found with ID {property_id}")

def refresh_properties():
    property_frame.pack_forget()
    show_properties()

root = tk.Tk()
root.title("Real Estate Listings")
root.configure(bg='lightblue')

title_label = tk.Label(root, text="Real Estate Listings", font=("Arial", 18), bg='lightblue')
title_label.pack()

property_frame = tk.Frame(root, bg='lightblue')

show_button = tk.Button(root, text="Show Properties", command=show_properties, bg='green', fg='white', width=20, height=2)
show_button.pack()

add_button = tk.Button(root, text="Add Property", command=add_property, bg='blue', fg='white', width=20, height=2)
add_button.pack()

delete_button = tk.Button(root, text="Delete Property", command=delete_property, bg='red', fg='white', width=20, height=2)
delete_button.pack()

root.mainloop()


