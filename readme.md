# Video Transcription Tool

This repository contains a Python tool for downloading videos from YouTube and transcribing their audio content into text using speech recognition.

## Setup

### Prerequisites

- Python 3.9.9 installed on your system
- pip package manager

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/k3smith/video-transcript-tool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd video-transcription-tool
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Download Videos (download.py)

The `download.py` script allows you to download videos from YouTube.

Usage:

```bash
python download.py
```

You will be prompted to enter the URL of the YouTube video and the directory where you want to save the video.

### 2. Transcribe Audio

The transcribe.py script transcribes the audio content of the downloaded YouTube videos into text using speech recognition from OpenAI's Whisper.

```bash
python transcript.py
```

The script will prompt you whether you'd like to trim the video content or not (Y/N). If you choose 'Y', it will trim the video content to the first 10 minutes plus 20% of the remainder before transcribing. If you choose 'N', it will transcribe the entire video.

The transcribed text will be saved in the 'transcripts' directory under a subdirectory named after the whisper model used for transcription.
