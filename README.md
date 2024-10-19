# Jarvis Voice Assistant

## Overview

Jarvis is a simple yet powerful voice assistant built in Python. It uses text-to-speech and speech recognition technologies to interact with users and perform various tasks. With Jarvis, you can search Wikipedia, open web pages, play music, check the time, and even send emails—all through voice commands.

## Features

- **Voice Interaction**: Engage with the assistant using natural voice commands
- **Wikipedia Search**: Quickly fetch and narrate information from Wikipedia
- **Web Browsing**: Open popular websites like YouTube, Google, and StackOverflow
- **Music Playback**: Play your favorite songs from a specified directory
- **Time Announcement**: Get the current time spoken out loud
- **Email Sending**: Send emails via Gmail using voice commands

## Requirements

- Python 3.x

## Installation

1. **Create a Virtual Environment** (optional but recommended):
   - Navigate to your project directory.
   - Create a virtual environment using the following command if not created:
     ```
     python -m venv .venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source .venv/bin/activate
       ```

2. **Install Required Packages**:
   - You can install all required packages in one go by using the `requirements.txt` file provided in this repository. Run the following command to install the packages:
     ```
     pip install -r requirements.txt
     ```

3. **Email Configuration**:
   - Replace `youremail@gmail.com` and `your-password` in the `sendEmail` function with your actual email credentials.
   - Adjust the `music_dir` and `codePath` variables to point to your music folder and code editor, respectively.

## Usage

1. **Run the Script**:
   - Ensure your virtual environment is activated.
   - Run the script with the following command:
     ```
     python jarvis.py
     ```

2. **Speak Your Command**:
   - When prompted, speak your command.
   - Use commands like:
     - "Wikipedia [topic]"
     - "Open YouTube"
     - "Play music"
     - "The time"
     - "Email to [name]"

## Security Note

Be cautious with email credentials. It's recommended to use environment variables or a secure credential store to handle sensitive information instead of hardcoding them in your script.

## License

This project is open-source and available under the MIT License.

## Author

Athithi Tyagi
