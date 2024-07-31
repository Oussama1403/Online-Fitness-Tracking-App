# Online Fitness Tracking App

## Overview

The Online Fitness Tracking App is a web application designed to help users track their fitness activities, monitor progress, and achieve their health goals. This application is built with a Flask backend and a Vue.js frontend, offering a responsive and user-friendly experience.

## Features

- **User Authentication**: Secure login and registration.
- **Fitness Tracking**: Log workouts, track progress, and set fitness goals.
- **Dashboard**: View summarized fitness data and analytics.
- **Responsive Design**: Optimized for various devices and screen sizes.

## Technologies Used

- **Backend**: Flask, SQLAlchemy, Flask-Migrate
- **Frontend**: Vue.js, Bootstrap
- **Database**: SQLite3
- **APIs**: Flask API endpoints for frontend-backend communication

## Installation

### Backend Setup

1. **Navigate to the Backend Directory**:
    ```sh
    cd Backend
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # For Command Prompt
    # .\venv\Scripts\Activate  # For PowerShell
    ```

3. **Install Required Python Packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask Server**:
    ```sh
    flask run
    ```

   The Flask server will start and be accessible at `http://localhost:5000`.

### Frontend Setup

1. **Navigate to the Frontend Directory**:
    ```sh
    cd Frontend/Vue
    ```

2. **Install Node.js and npm**:
   - Download and install from [Node.js](https://nodejs.org/).

3. **Install Project Dependencies**:
    ```sh
    npm install
    ```

4. **Run the Vue.js Development Server**:
    ```sh
    npm run dev
    ```

## Documentation

- [TODO.md](TODO.md): Tasks and features to be implemented.
- [SPECIFICATIONS.md](SPECIFICATIONS.md): Detailed project specifications.
- [CHANGELOG.md](CHANGELOG.md): Record of changes and updates.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to [obensassi.03@gmail.com].