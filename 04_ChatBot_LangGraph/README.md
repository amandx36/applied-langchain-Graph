# Joke Generator with Persistence

This project is a simple chatbot application built using LangGraph and Google's Generative AI (Gemini) that generates funny jokes on a given topic and provides explanations for them. It incorporates persistence through in-memory checkpoints to maintain conversation state across runs.

## Features

- **Joke Generation**: Generates humorous jokes based on user-specified topics using Google's Gemini AI model.
- **Explanation**: Provides detailed explanations of the generated jokes.
- **Streaming Output**: Supports real-time streaming of responses for a dynamic user experience.
- **Persistence**: Uses LangGraph's checkpointing mechanism to save and resume conversation states.
- **Graph-Based Workflow**: Implements a sequential workflow using LangGraph for structured processing.

## Requirements

- Python 3.8 or higher
- Google AI API key (for accessing Gemini models)
- Required Python packages:
  - `python-dotenv` (for loading environment variables)
  - `langchain-core` (for prompt templates)
  - `langgraph` (for graph-based workflows)
  - `langchain-google-genai` (for Google Generative AI integration)

## Installation

1. Clone or download the project files.
2. Install the required dependencies:
   ```
   pip install python-dotenv langchain-core langgraph langchain-google-genai
   ```
3. Create a `.env` file in the project root and add your Google AI API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

## Usage

1. Ensure your `.env` file is set up with the correct API key.
2. Run the script:
   ```
   python JokeGenerateWithPersistance.py
   ```
3. The script will generate a joke about "pizza" (hardcoded in the example) and its explanation, streaming the output in real-time.
4. To modify the topic, edit the `{"topic":"pizza"}` in the `workflow.stream()` call.

## Code Structure

### State Management
- `JokeState`: A TypedDict defining the state with fields:
  - `topic`: The subject for joke generation.
  - `joke`: The generated joke text.
  - `explanation`: The explanation of the joke.

### Nodes
- `generateJoke(state: JokeState)`: Generates a joke based on the topic using the LLM.
- `generateExplanation(state: JokeState)`: Explains the generated joke using the LLM.

### Graph Workflow
The workflow follows this sequence:
1. **Start** → Generate Joke
2. Generate Joke → Generate Explanation
3. Generate Explanation → **End**

### Persistence
- Uses `InMemorySaver` for checkpointing, allowing the graph to resume from previous states.
- Configured with a thread ID ("1") for session management.

### LLM Configuration
- Model: `gemini-3-flash-preview`
- Temperature: 0 (deterministic responses)
- Streaming: Enabled for real-time output
- Max retries: 2

## Output
The script streams the joke and explanation directly to the console. Example output might look like:
```
Why did the pizza go to therapy? Because it had too many toppings and felt crusty!

This joke plays on the word "crusty" which can mean both having a hard outer layer (like pizza crust) and being irritable or bad-tempered. The pizza "feels crusty" due to emotional issues from having too many toppings, creating a pun on the crust's texture and personality.
```

## Customization
- Change the topic by modifying the input dictionary in `workflow.stream()`.
- Adjust LLM parameters (temperature, model) in the `ChatGoogleGenerativeAI` initialization.
- Extend the graph by adding more nodes or edges for additional functionality.

## Notes
- This is a basic example demonstrating LangGraph's capabilities with AI integration.
- For production use, consider using persistent storage (e.g., database) instead of in-memory checkpoints.
- Ensure your Google AI API key has sufficient quota for the requests.