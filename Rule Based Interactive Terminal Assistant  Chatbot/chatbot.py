
import json
import re
from pathlib import Path
from datetime import datetime


# -------------------- Configuration --------------------

FAQ_FILE = Path(__file__).with_name("sample_faq.json")

DEFAULT_FAQS = {
    "business_hours": {
        "keywords": ["business hours", "opening hours", "working hours",
                     "open", "close", "timings"],
        "patterns": [
            r"\b(?:what are|tell me|show me)\b.*\b(?:hours|timings)\b",
            r"\bwhen\b.*\b(?:open|close)\b"
        ],
        "response": (
            "Our business hours are Monday to Friday, "
            "9:00 AM to 6:00 PM."
        )
    },
    "products": {
        "keywords": ["product", "products", "catalog", "catalogue"],
        "patterns": [
            r"\bwhat do you sell\b",
            r"\bshow me\b.*\bproducts\b"
        ],
        "response": (
            "We offer a range of products. Please tell me "
            "which product or category you are interested in."
        )
    },
    "pricing": {
        "keywords": ["price", "pricing", "cost", "charges", "fee"],
        "patterns": [
            r"\bhow much\b",
            r"\bwhat does it cost\b"
        ],
        "response": (
            "Product prices depend on the item. Please specify "
            "the product you want pricing information for."
        )
    },
    "shipping": {
        "keywords": ["shipping", "delivery", "dispatch", "shipment"],
        "patterns": [
            r"\bwhere is my order\b",
            r"\bdelivery time\b"
        ],
        "response": (
            "Delivery times depend on your location and product. "
            "Please check your order confirmation for tracking details."
        )
    },
    "returns": {
        "keywords": ["return", "refund", "exchange", "replacement"],
        "patterns": [
            r"\breturn policy\b",
            r"\bget my money back\b"
        ],
        "response": (
            "For returns or refunds, please check the applicable "
            "return policy or contact our support team with your order details."
        )
    },
    "contact": {
        "keywords": ["contact", "email", "phone", "support", "address"],
        "patterns": [
            r"\bhow can i reach you\b",
            r"\bcustomer service\b"
        ],
        "response": (
            "Please visit our official website for verified contact "
            "details and customer support information."
        )
    }
}

GREETINGS = {
    "hi": "Hello! Welcome to customer support.",
    "hello": "Hi there! How can I help you today?",
    "hey": "Hey! What can I help you with?"
}

EXIT_WORDS = {"bye", "goodbye", "exit", "quit"}


# -------------------- Load FAQ Data --------------------

def load_faqs():
    """Load FAQs from JSON, falling back to built-in FAQs."""
    if not FAQ_FILE.exists():
        return DEFAULT_FAQS.copy()

    try:
        with FAQ_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("FAQ data must be a JSON object.")

        # Validate individual FAQ entries.
        for intent, details in data.items():
            if not isinstance(details, dict):
                raise ValueError(f"Invalid FAQ entry: {intent}")

            if not isinstance(details.get("response"), str):
                raise ValueError(f"Missing response for: {intent}")

        return data

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"[Warning] Could not load FAQ file: {error}")
        print("[Info] Using built-in FAQs instead.")
        return DEFAULT_FAQS.copy()


# -------------------- Input Processing --------------------

def normalize_text(text):
    """Normalize user input for consistent matching."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s'-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def is_exit_command(text):
    """Check whether the complete message is an exit command."""
    return normalize_text(text) in EXIT_WORDS


def detect_greeting(text):
    """Identify greetings without matching words inside other words."""
    for greeting, response in GREETINGS.items():
        if re.search(rf"\b{re.escape(greeting)}\b", text):
            return response
    return None


# -------------------- Intent Matching --------------------

def detect_intents(text, faqs):
    """
    Match all relevant FAQ intents using keywords and regex.
    Return intents in the order they appear in the FAQ dictionary.
    """
    matched_intents = []

    for intent, details in faqs.items():
        keywords = details.get("keywords", [])
        patterns = details.get("patterns", [])

        # Match complete keywords or phrases.
        for keyword in keywords:
            keyword = str(keyword).lower().strip()

            if keyword and re.search(
                rf"(?<!\w){re.escape(keyword)}(?!\w)", text
            ):
                matched_intents.append(intent)
                break

        # Also support custom regular-expression patterns.
        if intent not in matched_intents:
            for pattern in patterns:
                try:
                    if re.search(pattern, text, re.IGNORECASE):
                        matched_intents.append(intent)
                        break
                except re.error:
                    print(f"[Warning] Invalid regex in FAQ: {intent}")

    return matched_intents


# -------------------- Conversation Management --------------------

def get_response(user_input, faqs, state):
    """Process input and return a response plus updated state."""
    text = normalize_text(user_input)

    if not text:
        return "Please enter a question so I can help.", state

    if is_exit_command(text):
        state["active"] = False
        return "Thank you for chatting with us. Goodbye!", state

    # Handle greetings.
    greeting = detect_greeting(text)

    # A greeting alone should not trigger FAQ matching.
    greeting_only = bool(
        re.fullmatch(r"(?:hi|hello|hey)[\s!.,'-]*", text)
    )

    if greeting_only:
        return greeting or "Hello! How can I help you?", state

    # Detect every matching intent, not just the first one.
    intents = detect_intents(text, faqs)

    responses = []

    if greeting:
        responses.append(greeting)

    for intent in intents:
        response = faqs[intent]["response"]
        responses.append(response)

    if intents:
        state["last_intents"] = intents
        return "\n".join(responses), state

    # Simple contextual follow-up handling.
    if state.get("last_intents"):
        return (
            "Could you clarify your question? For example, you can ask "
            "about business hours, products, pricing, delivery, or returns."
        ), state

    return (
        "I'm sorry, I didn't understand that question. "
        "Try asking about business hours, products, pricing, delivery, "
        "returns, or contact information."
    ), state


# -------------------- Main Chat Loop --------------------

def main():
    faqs = load_faqs()

    state = {
        "active": True,
        "last_intents": []
    }

    print("=" * 48)
    print("       CUSTOMER SUPPORT CHATBOT")
    print("=" * 48)
    print("Bot: Hello! How can I help you today?")
    print("Bot: Type 'bye', 'exit', or 'quit' to end.\n")

    while state["active"]:
        try:
            user_input = input("You: ")
            response, state = get_response(user_input, faqs, state)
            print(f"Bot: {response}\n")

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Chat session ended. Goodbye!")
            break

        except Exception as error:
            # Keep unexpected errors from crashing the conversation.
            print(f"Bot: Sorry, something went wrong. Please try again.")
            print(f"[Debug] {error}")


if __name__ == "__main__":
    main()
