# Heart Rate Estimation and Stress Level Measurement Web Application

This web application estimates heart rate and measures stress levels using physiological signals extracted from uploaded video files. It utilizes Python Flask as the backend framework and HTML/JavaScript for the frontend user interface.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/itz-salemm/BeatPal.git
```

2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

3. Set up environment variables for Firebase authentication. You can create a `.env` file in your project directory and add the following configuration:

```bash
FIREBASE_API_KEY=your_api_key
FIREBASE_AUTH_DOMAIN=your_auth_domain
FIREBASE_STORAGE_BUCKET=your_storage_bucket
```

## Usage

1. Run the Flask web server:

```
python app.py
```

2. Open your web browser and navigate to [http://localhost:5000/estimate](http://localhost:5000/estimate).

3. Upload a video file containing the subject's facial region.

4. Click the "Estimate Heart Rate" button.

5. The estimated heart rate and stress level will be displayed on the webpage.

## Features

- **Heart Rate Estimation**: The application calculates the heart rate of the subject by analyzing the facial region in the uploaded video.
- **Stress Level Measurement**: In addition to heart rate estimation, the application measures stress levels using heart rate variability (HRV) as an indicator.
- **User-friendly Interface**: The web interface allows users to easily upload video files and view the results.

## Project Structure

The project consists of the following components:

- `app.py`: The main Flask application file that defines routes and handles requests.
- `templates/index.html`: The HTML template for the user interface, including the file upload form and result display.
- `pulse_tracker.py`: The Python module containing the `Pulse` class for heart rate estimation and stress level measurement.

## Dependencies

- Flask: Lightweight web framework for Python.
- OpenCV: Library for computer vision tasks, used for video processing.
- NumPy: Library for numerical computations.
- SciPy: Library for scientific computing.
- Pyrebase: Python wrapper for Firebase, used for storage access (if applicable).
