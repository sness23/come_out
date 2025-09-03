# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python script that uses OpenAI's text-to-speech API to generate audio from text input. The script generates a WAV file containing the spoken text "come out to show them" using the GPT-4o mini TTS model with the "alloy" voice.

## Dependencies

The project requires:
- `openai` - OpenAI Python client library
- `soundfile` - Audio file I/O library (imported but not actively used in current implementation)

## Running the Code

To execute the text-to-speech generation:
```bash
python come_out.py
```

This will create a file called `come_out_to_show_them.wav` in the current directory.

## Architecture

The codebase consists of a single file (`come_out.py`) that:
1. Initializes an OpenAI client
2. Defines the text to be converted to speech
3. Makes an API call to OpenAI's TTS endpoint
4. Writes the audio response to a WAV file

## API Configuration

The script uses the OpenAI API and expects authentication via environment variables or API key configuration. The TTS model used is "gpt-4o-mini-tts" with the "alloy" voice profile.

## Common Issues

- **Rate Limit Error (429)**: If you encounter "insufficient_quota" errors, check your OpenAI account billing and usage limits at https://platform.openai.com/account/usage
- **Authentication**: Ensure your OpenAI API key is properly configured via environment variable `OPENAI_API_KEY` or other authentication methods