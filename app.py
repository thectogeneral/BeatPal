from flask import Flask, request, jsonify, render_template
from pulse import Pulse

app = Flask(__name__)
pulse_tracker = Pulse()

@app.route('/estimate', methods=['GET', 'POST'])
def estimate_heart_rate_and_stress():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400

        video_file = request.files['video']
        video_file.save('input_video.mp4')

        pulse_tracker.video_to_frames('input_video.mp4')
        heart_rate = pulse_tracker.bpm()
        stress_level = pulse_tracker.calculate_hrv()  # Assuming you have a method for stress level calculation

        if heart_rate is not None and stress_level is not None:
            return jsonify({'heart_rate': heart_rate, 'stress_level': stress_level}), 200
        else:
            return jsonify({'error': 'Heart rate or stress level calculation failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
