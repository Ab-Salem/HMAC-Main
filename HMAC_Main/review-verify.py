import hmac
import hashlib
import json
import base64

SECRET_KEY = b'bookworm2024'  # Authentication key for book reviews


def verify_review_signature(review_data: dict, signature: str) -> bool:
    """Check if the book review is authentic and unmodified."""
    content = json.dumps(review_data, separators=(',', ':')).encode('utf-8')
    calculated_hash = hmac.new(SECRET_KEY, content, hashlib.sha256).digest()
    expected_signature = base64.b64encode(calculated_hash).decode()

    return hmac.compare_digest(signature, expected_signature)


def process_review():
    """Handle incoming book review and verify its authenticity."""
    # Read the review from storage
    with open("review_data.json", "r") as f:
        review_package = json.load(f)

    incoming_review = review_package["review_content"]
    review_signature = review_package["signature"]

    if verify_review_signature(incoming_review, review_signature):
        print("✓ Review verification passed - content is authentic")
        print("Review details:", incoming_review)
    else:
        print("✗ Review verification failed - content may be modified")


if __name__ == "__main__":
    process_review()