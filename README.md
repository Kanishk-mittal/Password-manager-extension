# Password Manager Extension

Welcome to the Password Manager Extension! This project is a secure, industry-grade password management solution developed by the **Beta Labs Cybersecurity Division**. It helps users generate, store, and manage strong passwords directly within their browser, ensuring both convenience and security.

---

## 🌟 Features

- **Secure Storage**: Passwords are encrypted and stored securely using MongoDB or you can even choose to store them on localstorage.
- **Autofill Support**: Automatically fill in credentials on websites.
- **Customizable Settings**: Choose themes, set auto-lock timers, and enable/disable autofill through the options page.
- **Cross-Platform Sync**: Sync settings and passwords across devices using Chrome's storage API.

---

## 📖 Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Related Files](#related-files)

---

## 🚀 Getting Started

Follow these steps to set up and use the Password Manager Extension:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/password-manager.git
   cd passwordManager
   ```

2. **Set Up the Backend**:
   - Move to the `backend/` directory:
     ```bash
     cd backend
     ```
   - Create a virtual environment:
     ```bash
     python -m venv .venv
     .\.venv\Scripts\activate
     ```
   - Install required Python dependencies:
     ```bash
     pip install -r backend/requirements.txt
     ```
   - create a `.env` file in backend folder and add the following:
     ```bash
      MONGO_URI=mongodb://localhost:27017/
      DB_NAME=SecurePass
      SENDER_EMAIL=youremail@gmail.com
      SENDER_PASSWORD=yourpassword
       ```
    - Ensure MongoDB is running on your system

3. **Run the Backend**:
   ```bash
   python backend/wsgi.py
   ```

4. **Load the Chrome Extension**:
   - Go to `chrome://extensions/` in your browser.
   - Enable **Developer Mode**.
   - Click on **Load unpacked** and select the `extension/` folder.

5. **Test the Application**:
   - Use the browser to interact with the extension and verify functionality.

---

## 📋 Usage

1. **Adding Passwords**:
   - Use the extension popup to save new credentials for websites.
2. **Managing Passwords**:
   - Access saved passwords through the popup or options page.
3. **Autofill Credentials**:
    - Enable autofill to automatically populate login forms on websites.
4. **Generating Passwords**:
    - Use the password generator to create strong, unique passwords.
5. **Syncing Data**:
    - Sync settings and passwords across devices using Chrome's storage API.
6. **Customizing Settings**:
   - Open the options page to configure themes, auto-lock timers, and more.

---

## 🤝 Contributing

We welcome contributions to this project! Follow the steps below to get involved:

1. Check out our [Contributing Guide](docs/CONTRIBUTING.md) for detailed instructions.
2. Report bugs or suggest features in the [Issues](https://github.com/<your-username>/password-manager/issues) section.
3. Create pull requests with well-documented and tested changes.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this project. However, the contributors are not liable for any misuse or damages.

---

## ✉️ Contact

For inquiries, feedback, or collaboration, contact the Beta Labs Cybersecurity Division:
- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **Website**: [Beta Labs](https://your-club-website.com)

---

## 🛡️ Disclaimer

This project is developed for educational purposes and is not intended for handling highly sensitive or critical data in production environments.

Test Sentence