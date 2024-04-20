import numpy as np
import cv2 as cv
from scipy.signal import argrelmin

class Stress(object):
    """
    This class provides methods to calculate stress level.
    """

    def __init__(self, frame_rate=30):
        """
        Initialise the Stress class. It takes one argument frame_rate
        which defaults to 30.
        """
        self.frame_rate = frame_rate

    def calculate_hrv(self, peaks):
        """
        Calculates the heart rate variability (HRV), which can be indicative of stress levels.
        """
        try:
            if peaks is None or len(peaks) < 2:
                return None

            rr_intervals = np.diff(peaks.flatten()) / self.frame_rate
            return np.std(rr_intervals)
        except Exception as e:
            print("Error calculating HRV:", e)
            return None

    def get_minima(self, variance):
        """
        Identifies the minima in the variance array.
        """
        try:
            minima = argrelmin(variance)
            minima = np.asarray(minima)
            final_minima = minima[
                (minima > self.frame_rate * 60 / 200)
            ]  # Filters values less than 9
            return final_minima
        except Exception as e:
            print("Error identifying minima:", e)
            return None

    def process_video(self, video_path):
        """
        Processes the uploaded video to calculate peaks and variance.
        """
        try:
            capture = cv.VideoCapture(video_path)
            peaks = []
            variance = []

            while True:
                ret, frame = capture.read()
                if not ret:
                    break

                # Process frame to extract necessary data
                # For example, you can calculate the average intensity of each frame
                gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                avg_intensity = np.mean(gray_frame)

                # Store the processed data
                peaks.append(avg_intensity)
                variance.append(avg_intensity)

            capture.release()

            return np.array(peaks), np.array(variance)
        except Exception as e:
            print("Error processing video:", e)
            return None, None


