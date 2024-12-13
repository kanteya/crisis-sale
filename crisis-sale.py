import openai
from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask, render_template, jsonify
import config
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

YOUTUBE_URL = "https://www.youtube.com/watch?v=SWECAhXgCOI"

def get_video_id(url):
    parsed_url = urlparse(url)
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    elif parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query).get("v", [None])[0]
        elif parsed_url.path.startswith("/embed/"):
            return parsed_url.path.split("/embed/")[1]
        elif parsed_url.path.startswith("/v/"):
            return parsed_url.path.split("/v/")[1]
    return None

def fetch_transcript(video_id):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def format_transcript(transcript):
    return '\n'.join([x['text'] for x in transcript])

def summarize_transcript(transcript):
    prompt = (
        "Summarize the following transcript as if you are a financial advisor."
        "Provide a concise summary of the Nifty and Sensex market movements in bullet points. Include a clear headline with specific numbers such as points gained or lost and percentage change. Only use the information from the transcript, without adding any external data or context. Focus solely on important details and group related points to enhance clarity. Avoid language that suggests staying informed, tracking trends, or making decisions. Do not provide trading advice, suggestions, or general reminders. Present the information in a simple, point-by-point format, highlighting the factors influencing the market. Do not include any asterisks in the response at any cost:\n\n"
        f"{transcript}"
    )
    
    try:
        openai.api_key = config.OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response['choices'][0]['message']['content']
        return summary
    except Exception as e:
        print(f"Error summarizing transcript: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html', url=YOUTUBE_URL)

@app.route('/fetch_summary')
def fetch_summary():
    video_id = get_video_id(YOUTUBE_URL)
    if not video_id:
        return jsonify(summary="Invalid YouTube URL.")
    
    transcript = fetch_transcript(video_id)
    summary = None
    if transcript:
        formatted_transcript = format_transcript(transcript)
        summary = summarize_transcript(formatted_transcript)
    return jsonify(summary=summary or "No summary available.")

if __name__ == "__main__":
    app.run(debug=True)