# ELSA - Chat Application with GUI

ELSA (Emulated Learning and Speech Assistant) is a Python-based chat application with a graphical user interface (GUI) built using Tkinter. It allows users to interact with a chatbot that can respond to predefined questions, provide current date and time, display images, and optionally convert text responses to speech using pyttsx3.

## Features

- **Graphical User Interface**: Built using Tkinter for a user-friendly chat experience.
- **Chatbot Capabilities**: Responds to predefined questions and commands.
- **Date and Time**: Provides current date and time upon request.
- **Image Display**: Can display random images from a specified folder.
- **Text-to-Speech**: Option to convert chat responses into speech.

## Requirements

- Python 3.x
- Tkinter
- Pillow (PIL)
- pyttsx3

## Usage

1. **Installation**: Ensure Python and the required libraries are installed.
   
2. **Run the Application**:
   ```bash
   python Elsa.py
   ```

3. **Interaction**:
   - Type your messages in the entry field and press `Enter` or click `Send`.
   - Use commands like `hi`, `date`, `time`, `clear`, and `bye` for specific responses.
   - Typing `pic` will display a random image from the `img` folder.

4. **Text-to-Speech**:
   - Click the `Text to Speech` button to toggle speech synthesis on or off.
   - Note: Speech synthesis requires speakers or headphones connected to hear the output.

5. **Clear Chat**:
   - Click `Clear Chat` to erase all messages from the chat window.

## JSON Dataset

- The chatbot's responses are based on a predefined set of questions and answers stored in `knowledge_base.json`.

## Contributing

- Contributions are welcome! Feel free to open issues or pull requests for any improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

