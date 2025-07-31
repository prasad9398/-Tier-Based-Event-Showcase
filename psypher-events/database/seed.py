from app import app
from database.models import db, Event
from datetime import datetime

sample_events = [
    {
        "title": "Free Concert",
        "description": "Enjoy a free outdoor concert in the park",
        "event_date": datetime(2025, 9, 15, 19, 0),
        "image_url": "/static/images/Free Concert Night.jpg",
        "tier": "free"
    },
    {
        "title": "Art Exhibition",
        "description": "Local artists showcase their work",
        "event_date": datetime(2025, 9, 20, 10, 0),
        "image_url": "/static/images/Local Art Fair.jpg",
        "tier": "free"
    },
    {
        "title": "Silver Lounge Access",
        "description": "Exclusive wine tasting event for Silver members",
        "event_date": datetime(2025, 9, 25, 18, 0),
        "image_url": "/static/images/Silver Lounge Access.jpg",
        "tier": "silver"
    },
    # Add more events for all tiers
]

with app.app_context():
    for event_data in sample_events:
        event = Event(**event_data)
        db.session.add(event)
    db.session.commit()
    print("Sample events added to database")