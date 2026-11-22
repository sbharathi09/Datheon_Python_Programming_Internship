# Rule-Based Interactive Terminal Assistant Chatbot

## 📌 Project Overview

The Rule-Based Interactive Terminal Assistant Chatbot is a Python-based conversational application that provides automated responses to common customer support queries. It uses keyword matching, regular expressions, and predefined FAQ responses to identify user intents and respond accordingly.

The chatbot runs in the terminal and supports greetings, business hours, product information, pricing, delivery, returns, and contact-related queries. It also handles multiple intents in a single message and provides fallback responses for unrecognized questions.

## 🎯 Objectives

- Develop an interactive terminal-based chatbot.
- Identify user intents using keywords and regular expressions.
- Provide predefined responses to frequently asked questions.
- Support multiple intents in a single query.
- Load FAQ data from a JSON file.
- Handle invalid input, missing files, and unexpected errors gracefully.
- Implement clean exit commands.

## ✨ Features

- **Interactive conversation:** Accepts user input continuously through the terminal.
- **Greeting detection:** Responds to greetings such as `hello`, `hi`, and `hey`.
- **FAQ handling:** Answers questions about business hours, products, pricing, shipping, returns, and contact information.
- **Regex-based matching:** Uses regular expressions to recognize common question patterns.
- **Multi-intent matching:** Identifies multiple supported topics in a single message.
- **JSON integration:** Loads customizable FAQ responses from a JSON dataset.
- **Fallback handling:** Provides helpful suggestions when a query is not recognized.
- **Error handling:** Handles missing or invalid FAQ files and unexpected runtime errors.
- **Exit commands:** Supports `bye`, `goodbye`, `exit`, and `quit`.

## 🛠️ Technologies Used

- Python 3.13
- Regular Expressions (`re`)
- JSON (`json`)
- Date and Time (`datetime`)
- File Handling (`pathlib`)

No third-party Python packages are required.

## 📂 Project Structure

```text
Rule Based Interactive Terminal Assistant Chatbot/
│
├── chatbot.py
├── sample_faq.json
└── README.md
```

### File Description

- `chatbot.py` — Contains the chatbot logic, intent detection, response generation, and conversation loop.
- `sample_faq.json` — Stores customizable FAQ keywords, regex patterns, and predefined responses.
- `README.md` — Documents the project, setup instructions, features, and usage.

The chatbot includes built-in FAQ responses if the JSON file is missing or cannot be loaded.

## ⚙️ Prerequisites

- Python 3.10 or later.
- Visual Studio Code or another code editor.
- PowerShell, Command Prompt, or a terminal.

Verify your Python installation:

```powershell
py --version
```

## 🚀 Installation and Execution

### Step 1: Open the project directory

Open the project folder in VS Code and open its integrated terminal.

### Step 2: Verify the files

Ensure that `chatbot.py` is present in the current directory. Add `sample_faq.json` if you want to customize the FAQs.

### Step 3: Run the chatbot

On Windows, execute:

```powershell
py chatbot.py
```

### Step 4: Interact with the chatbot

Enter your question when the `You:` prompt appears. The chatbot displays its response and waits for the next message.

### Step 5: Exit the conversation

Type any supported exit command:

```text
bye
exit
quit
```

## 💬 Sample Interaction

```text
================================================
       CUSTOMER SUPPORT CHATBOT
================================================
Bot: Hello! How can I help you today?
Bot: Type 'bye', 'exit', or 'quit' to end.

You: hello
Bot: Hi there! How can I help you today?

You: What are your business hours?
Bot: Our business hours are Monday to Friday, 9:00 AM to 6:00 PM.

You: Tell me your products and delivery options.
Bot: We offer a range of products. Please tell me
which product or category you are interested in.
Delivery times depend on your location and product.
Please check your order confirmation for tracking details.

You: exit
Bot: Thank you for chatting with us. Goodbye!
```

*Note: The business hours and other FAQ responses are demonstration data and should be customized for a real business.*

## 🧠 How It Works

1. **Input collection:** Accepts a message from the user.
2. **Normalization:** Converts text to lowercase, removes unnecessary whitespace, and normalizes punctuation.
3. **Greeting and exit detection:** Identifies greetings and commands that end the session.
4. **Intent identification:** Matches keywords and regular expressions against the configured FAQ categories.
5. **Response generation:** Returns the predefined responses for all recognized intents.
6. **Fallback handling:** Suggests supported topics when no intent matches.
7. **Conversation management:** Continues processing messages until the user exits or interrupts the session.

## 🧪 Testing

Test the chatbot using the following scenarios:

| Test Case | Input | Expected Result |
|---|---|---|
| Greeting | `hello` | Displays a greeting |
| Business hours | `What are your business hours?` | Displays business hours |
| Product query | `Tell me about your products` | Displays product information |
| Pricing query | `What is the price?` | Requests product details |
| Multiple intents | `Tell me about products and delivery` | Displays both matching responses |
| Unknown query | `Tell me a joke` | Displays a fallback response |
| Exit command | `quit` | Ends the conversation |
| Empty input | Press Enter without typing | Requests a question |
| Missing JSON file | Remove or rename `sample_faq.json` | Uses built-in FAQs |

## ⚠️ Limitations

- Uses predefined rules rather than machine learning or natural language understanding.
- Recognizes only the keywords and patterns configured in the FAQ data.
- Does not retrieve live business information or order status.
- Does not connect to a database or external customer support service.
- Contextual follow-up handling is basic and does not fully resolve references to previous messages.

## 🔮 Future Enhancements

- Integrate an NLP model for improved intent classification.
- Add conversation memory for contextual follow-up questions.
- Connect to a database for customer and order information.
- Integrate a real product catalogue and order-tracking API.
- Add logging and automated unit tests.
- Develop a graphical interface or web-based chatbot.
- Integrate a retrieval-augmented generation (RAG) pipeline for answering questions from business documents.

## 📚 Learning Outcomes

This project demonstrates practical use of:

- Python functions, dictionaries, and control flow.
- String processing and regular expressions.
- JSON parsing and file handling.
- Intent matching and multi-intent response generation.
- Exception handling and interactive application design.

## 👩‍💻 Author

**Swamidas Bharathi**

GitHub: [sbharathi09](https://github.com/sbharathi09)

---

## 📄 License

This project is intended for educational and learning purposes. Add an appropriate open-source license if you plan to distribute it publicly.
