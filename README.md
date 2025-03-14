# WAbot - WhatsApp Automation Library

WAbot is a Python library designed to automate interactions with WhatsApp Web using Selenium. With this library, you can automate tasks such as sending messages, checking if a phone number is registered on WhatsApp, and more. This library is ideal for developers looking to integrate WhatsApp automation into their Python-based applications or projects.

## Features

- **Headless Browser Automation**: Uses Selenium and ChromeDriver for headless browser automation.
- **Login Automation**: Waits for WhatsApp Web QR code and allows saving it for later use.
- **Message Sending**: Sends messages with a humanized delay for a more natural experience.
- **Contact Navigation**: Goes to a specific contact by name or navigates to an unknown phone number.
- **Random Advertisement Sending**: Sends a random advertisement from a list of pre-defined ads.
- **Message Retrieval**: Retrieves the most recent message and its sender.
- **Error Handling**: Handles potential errors during interactions, such as missing elements or failed actions.
- **Screenshot**: Takes screenshots for debugging or logging purposes.

## Installation

1. Ensure you have Python 3.6 or higher installed.
2. Install the required dependencies:

```bash
pip install selenium webdriver-manager
```

3. Install the WAbot library:

```bash
pip install git+https://github.com/EhanChowdhury/WAbot.git
```

## Usage

### Initialize WAbot

```python
from WAbot import WAbot

# Create an instance of WAbot
bot = WAbot(verbose=True, saveQR=False, headless=False)
```

### Go to a Contact

Navigate to a specific contact by name:

```python
bot.go_to_contact('John Doe')
```

### Send a Message

Send a message to the currently selected contact:

```python
bot.send_message('Hello! This is an automated message.', humanize=2)
```

### Check if a Phone Number is on WhatsApp

Check if a specific phone number is registered on WhatsApp:

```python
is_wa = bot.check_if_wa('+1234567890')
print(is_wa)  # True if on WhatsApp, False otherwise
```

### Send a Random Advertisement

Send a random advertisement from a predefined list of ads:

```python
ads = [
    {'Message': 'Buy one, get one free!', 'Sender': 'Company A'},
    {'Message': '50% off on all products!', 'Sender': 'Company B'}
]

bot.send_random_ad(ads, humanize=2)
```

### Get the Latest Message

Retrieve the latest message in the chat:

```python
message = bot.get_message()
print(message)
```

### Take a Screenshot

Save a screenshot of the current WhatsApp Web page:

```python
bot.save_screenshot('whatsapp_screenshot.png')
```

## Arguments

- `verbose` (bool): Whether to print logs to the console (default: `True`).
- `saveQR` (bool): Whether to save the QR code as a screenshot (default: `False`).
- `humanize` (int): Time delay (in seconds) to humanize actions like typing and sending messages.
- `headless` (bool): Whether to run the program in headless mode (default: `False`).
- `sandbox` (bool): Whether to use a sandbox environment (default: `True`).
- `shm` (bool): Whether to enable shared memory (default: `True`).  

## Dependencies

- Python 3.6+
- [Selenium](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute by creating issues or submitting pull requests. For any questions or feedback, open an issue in the repository!
