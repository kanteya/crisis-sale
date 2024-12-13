# CRISIS SALE

This project fetches transcripts from YouTube videos and generates concise financial summaries using OpenAI's GPT model. It focuses on summarizing Nifty and Sensex market movements into actionable insights while adhering to strict constraints on language and content.

## Features
- Extracts transcripts from YouTube videos using `youtube_transcript_api`.
- Processes and formats the transcript into a readable format.
- Summarizes the transcript using OpenAI's GPT model.
- Delivers bullet-point financial summaries based only on the content of the video transcript.
- Flask-based web interface to fetch and display summaries.

## Prerequisites
To run this project, ensure you have the following:
- Python 3.8 or higher
- Flask
- `youtube_transcript_api`
- `openai` Python package
- OpenAI API key
- A valid YouTube video URL containing a transcript

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/youtube-financial-summary.git
cd youtube-financial-summary
```

### 2. Install Dependencies
Use pip to install the required dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `config.py` file in the project root directory and add your OpenAI API key
```python
# config.py
OPENAI_API_KEY = "your-openai-api-key"
```

### 4. Update YouTube URL
In the `app.py` file, replace the YOUTUBE_URL with the URL of the desired YouTube video
```python
YOUTUBE_URL = "https://www.youtube.com/watch?v=SWECAhXgCOI"
```

## How to Run

### 1. Start the Flask Server
Run the application
```bash
python crisis-sale.py
```

### 2. Access the Application
Open your browser and navigate to
```
(http://127.0.0.1:5000/)
```

### 3. Fetch Summary
1. The home page will display the configured YouTube URL.
2. Visit `/fetch_summary` to get the transcript summary as JSON.

## Project Summary
```bash
.
├── app.py               # Main Flask application
├── config.py            # Configuration file for API keys
├── templates/
│   └── index.html       # HTML template for the home page
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

## Dependencies
1. Flask
2. youtube_transcript_api
3. openai

```bash
pip install flask youtube_transcript_api openai
```

## Future Improvements
1. Add an enhanced user interface with data visualization.
2. Enhance error handling for missing or unavailable transcripts.
3. Implement additional summarization models for different contexts
