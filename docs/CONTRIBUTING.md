# Contributing to Password Manager Project

Thank you for considering contributing to this project! We welcome contributions to improve the functionality, fix bugs, enhance documentation, or add new features.

---

## Getting Started

1. **Fork the Repository**  
   Fork the repository on GitHub to your own account.

2. **Clone the Repository**  
   Clone the forked repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/password-manager.git
   cd password-manager
   ```

3. **Set Up the Environment**  
   Install the necessary dependencies for the backend:
   ```bash
   pip install -r backend/requirements.txt
   ```
   Ensure MongoDB is running on your system and configure the connection in `backend/app/config.py`.

4. **Run the Backend**  
   Start the Flask server:
   ```bash
   python backend/wsgi.py
   ```

5. **Load the Chrome Extension**  
   - Go to `chrome://extensions/` in your browser.
   - Enable **Developer Mode**.
   - Click on **Load unpacked** and select the `extension/` folder.

6. **Test the Application**  
   Verify the application is running as expected before making changes.

---

## Contribution Guidelines

- **Issues:**  
  Before starting work, check if the issue you want to address is already reported in the [Issues](https://github.com/<repo-owner>/password-manager/issues) section. If not, create a new issue with a detailed description.

- **Feature Requests:**  
  For new features, open an issue describing the functionality and its benefits.

- **Coding Standards:**  
  - Use meaningful variable and function names.
  - Comment your code for better readability.

- **Commit Messages:**  
  Use clear and concise commit messages. Example:
  ```
  Add: Encryption feature for saved passwords
  Fix: Bug in user authentication
  ```

- **Pull Requests:**  
  - Make sure your branch is up-to-date with the `main` branch before creating a pull request:
    ```bash
    git checkout main
    git pull origin main
    ```
  - Submit your pull request to the `main` branch.
  - Include a detailed description of your changes and reference the related issue (if applicable).

---

## Community Standards

- Be respectful and collaborative.
- Avoid submitting incomplete work unless it is marked as a draft pull request.
- Ensure your contributions align with the project's purpose and goals.

---

Thank you for your interest in contributing! If you have any questions or need clarification, feel free to reach out by opening an issue or contacting us directly.