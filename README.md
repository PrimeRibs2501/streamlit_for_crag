# Streamlit for CRAG

![Streamlit Logo](https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png)  
![Docker Logo](https://iconduck.com/icons/677/docker)  
![Python Logo](https://www.iconfinder.com/icons/4518857/python_icon)

A **Streamlit** application designed to streamline and enhance CRAG-related workflows. This project leverages **Python** and **Docker** to provide an efficient and scalable solution.

---

## 📋 Table of Contents

- [About](#about)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🛠️ About

The **Streamlit for CRAG** project is a web application built using Streamlit, designed to simplify tasks related to CRAG (Custom Resource Allocation Generator). It provides an intuitive interface for users and integrates seamlessly with Docker for deployment.

This repository includes:
- A Python-based Streamlit app (`streamlit_for_crag.py`).
- Configuration files (`settings.py`, `.env`) for customization.
- Docker support for containerized deployment.

---

## 🖥️ Technologies Used

This project utilizes the following technologies:
- **Python**: Main programming language.
- **Streamlit**: Framework for building interactive web applications.
- **Docker**: For containerization and deployment.
- **Poetry**: Dependency management tool.

---

## 🚀 Installation

Follow these steps to set up the project locally:

1. Clone the repository:
git clone https://github.com/PrimeRibs2501/streamlit_for_crag.git
cd streamlit_for_crag

text

2. Install dependencies using Poetry:
poetry install

text

3. Set up environment variables:
- Create a `.env` file in the root directory.
- Add necessary configurations (refer to `settings.py`).

4. Run the application:
streamlit run streamlit_for_crag.py

text

---

## 📚 Usage

To use the application:

1. Start the Streamlit server by running the command above.
2. Open your browser and navigate to `http://localhost:8501`.
3. Interact with the CRAG-related tools provided by the app.

For Docker-based deployment:
docker build -t streamlit_for_crag .
docker run -p 8501:8501 streamlit_for_crag

text

---

## 📂 Folder Structure

Below is an overview of the project's folder structure:

├── docker/ # Docker-related files
├── .env # Environment variables
├── .gitignore # Git ignore rules
├── poetry.lock # Dependency lock file
├── pyproject.toml # Project configuration file (Poetry)
├── settings.py # Application settings
├── streamlit_for_crag.py # Main Streamlit app script

text

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Create a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
