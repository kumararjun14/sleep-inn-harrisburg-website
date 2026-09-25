"""Hotel portfolio concept with room previews and non-delivering demo forms."""
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import date
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") or os.urandom(32)

HOTEL = {
    "name": "Sleep Inn & Suites Harrisburg / Hershey North",
    "short_name": "Sleep Inn Harrisburg",
    "location": "Harrisburg, PA near Hersheypark",
    "phone": "",
    "email": "",
    "address": "Harrisburg / Hershey North, PA",
    "maps_query": "Sleep Inn & Suites Harrisburg Hershey North",
}

ROOM_TYPES = [
    {
        "slug": "double-queen",
        "name": "Double Queen Room",
        "beds": "2 Queen Beds",
        "size": "340 sq ft",
        "guests": 4,
        "tag": "Room style",
        "image": "https://images.unsplash.com/photo-1566665797739-1674de7a421a?auto=format&fit=crop&w=1400&q=80",
        "description": "A bright, flexible room designed for families, friends, tournament weekends, and road trips. Two plush queen beds, layered lighting, a workspace, mini-fridge, and plenty of storage make it easy to settle in.",
        "features": ["Two queen beds", "Mini-fridge and microwave", "Work desk", "Smart TV", "Coffee station", "USB charging"],
    },
    {
        "slug": "single-king",
        "name": "Single King Room",
        "beds": "1 King Bed",
        "size": "315 sq ft",
        "guests": 2,
        "tag": "Room style",
        "image": "https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1400&q=80",
        "description": "A calm and polished retreat with one oversized king bed, soft textures, a generous work corner, and blackout curtains for a deeper night of rest.",
        "features": ["King bed", "Lounge chair", "Blackout curtains", "Walk-in shower", "Smart TV", "Premium linens"],
    },
    {
        "slug": "king-suite",
        "name": "Single King Suite",
        "beds": "1 King Bed + Sofa Area",
        "size": "520 sq ft",
        "guests": 3,
        "tag": "Suite style",
        "image": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=1400&q=80",
        "description": "Our largest room type, created for longer stays, special weekends, and guests who want extra space. Enjoy a separate sitting area, upgraded bath amenities, and a more private suite-style layout.",
        "features": ["King bed", "Separate sitting area", "Sleeper sofa", "Large vanity", "Upgraded bath amenities", "Dining nook"],
    },
]

AMENITIES = [
    ("Free Wi-Fi", "Fast wireless internet throughout the hotel."),
    ("Hot Breakfast", "Waffles, eggs, fruit, coffee, and quick grab-and-go options."),
    ("24/7 Front Desk", "Friendly help anytime you arrive or need assistance."),
    ("Fitness Room", "Cardio, weights, towels, and filtered water."),
    ("Free Parking", "Simple parking with easy entrance access."),
    ("Business Corner", "Printer access, workspace, and charging stations."),
]

GALLERY = [
    "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?auto=format&fit=crop&w=1200&q=80",
    "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?auto=format&fit=crop&w=1200&q=80",
]

@app.context_processor
def inject_globals():
    return {"current_year": date.today().year, "hotel": HOTEL, "site_url": os.getenv("SITE_URL", "").rstrip("/")}

@app.route("/")
def home():
    return render_template("index.html", rooms=ROOM_TYPES, amenities=AMENITIES, gallery=GALLERY, page_title="Hotel near Hersheypark | Sleep Inn Harrisburg")

@app.route("/rooms")
def rooms():
    return render_template("rooms.html", rooms=ROOM_TYPES, page_title="Rooms & Suites | Sleep Inn Harrisburg")

@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        flash("Portfolio demo: no booking request was sent or saved. Use the official hotel booking channel.", "notice")
        return redirect(url_for("booking"))
    return render_template("booking.html", rooms=ROOM_TYPES, selected_slug=request.args.get("room", ""),
                           page_title="Booking Request | Sleep Inn Harrisburg")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Portfolio demo: your message was not sent or saved. Use an official hotel contact channel.", "notice")
        return redirect(url_for("contact"))
    return render_template("contact.html", page_title="Contact | Sleep Inn Harrisburg")

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
