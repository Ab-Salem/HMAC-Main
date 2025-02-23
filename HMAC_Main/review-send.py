import hmac
import hashlib
import json
import base64

SECRET_KEY = b'bookworm2024'  # Authentication key for book reviews


def create_review_signature(review_data: dict) -> str:
    """Create a digital signature for the book review."""
    content = json.dumps(review_data, separators=(',', ':')).encode('utf-8')
    hash_value = hmac.new(SECRET_KEY, content, hashlib.sha256).digest()
    return base64.b64encode(hash_value).decode()


def submit_review():
    """Submit a new book review with security verification."""
    review_data = {
        "reviewer": "BookLover123",
        "book_title": "The Digital Fortress",
        "rating": 4.5,
        "verified_purchase": True
    }

    review_signature = create_review_signature(review_data)
    review_package = {
        "review_content": review_data,
        "signature": review_signature
    }

    # Save the review to storage
    with open("review_data.json", "w") as f:
        json.dump(review_package, f)

    print("Review submitted with verification:", review_package)


if __name__ == "__main__":
    submit_review()