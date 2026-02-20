# 🧠 Emotion Detector

A web application that analyzes text and detects the dominant emotion using IBM Watson's NLP Emotion Prediction API. Built with Python and Flask.

## 📋 Features

- Detects **5 core emotions** from any text input:
  - 😠 Anger
  - 🤢 Disgust
  - 😨 Fear
  - 😊 Joy
  - 😢 Sadness
- Identifies the **dominant emotion** from the analysis
- Clean web interface for real-time text analysis
- Graceful error handling for blank or invalid input

## 🗂️ Project Structure

```
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py               # Package initializer
│   ├── emotion_detection.py      # Core emotion detection logic
│   ├── server.py                 # Flask web server
│   └── test_emotion_detection.py # Unit tests
├── templates/
│   └── index.html                # Frontend HTML template
├── static/
│   └── mywebscript.js            # Frontend JavaScript
└── README.md
```

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **NLP API:** [IBM Watson NLP Emotion Predict](https://sn-watson-emotion.labs.skills.network)
- **Frontend:** HTML, JavaScript
- **Testing:** Python `unittest`

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/emotion-detector.git
   cd emotion-detector
   ```

2. **Install dependencies:**
   ```bash
   pip install flask requests
   ```

### Running the Application

Start the Flask server from the project root:

```bash
python EmotionDetection/server.py
```

Then open your browser and navigate to:

```
http://localhost:5000
```

Enter any text in the textarea and click **"Run Sentiment Analysis"** to see the emotion scores and dominant emotion.

## 🔌 API Endpoint

| Method | Endpoint | Query Parameter | Description |
|--------|----------|-----------------|-------------|
| `GET` | `/emotionDetector` | `textToAnalyze` | Returns emotion scores and dominant emotion |

**Example request:**
```
GET /emotionDetector?textToAnalyze=I am so happy today!
```

**Example response:**
```
For the given statement, the system response is 'anger': 0.006, 'disgust': 0.002,
'fear': 0.009, 'joy': 0.956 and 'sadness': 0.027. The dominant emotion is joy.
```

## 🧪 Running Tests

Run the unit tests from the project root:

```bash
python -m pytest EmotionDetection/test_emotion_detection.py -v
```

Or using `unittest` directly:

```bash
python -m unittest EmotionDetection/test_emotion_detection.py
```

The test suite covers all five emotion categories:

| Test | Input Text | Expected Dominant Emotion |
|------|-----------|---------------------------|
| `test_joy` | "I am glad this happened" | `joy` |
| `test_anger` | "I am really mad about this" | `anger` |
| `test_disgust` | "I feel disgusted just hearing about this" | `disgust` |
| `test_sadness` | "I am so sad about this" | `sadness` |
| `test_fear` | "I am really afraid that this will happen" | `fear` |

## ⚠️ Error Handling

- If the input text is **blank or invalid**, the API returns a `400` status code, and the application responds with:
  ```
  Invalid text! Please try again!
  ```

## 📄 License

This project is for educational purposes as part of an IBM Skills Network course.
