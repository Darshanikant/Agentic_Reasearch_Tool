# utils/summarize.py

from agent_config import summarizer_chain

def summarize_results(results):
    """Summarizes web search results using Gemini."""
    combined_text = ""
    for i, result in enumerate(results, start=1):
        combined_text += f"{i}. {result['title']}\n{result['body']}\n\n"

    # Run through Gemini
    summary = summarizer_chain.run(text=combined_text)
    return summary.strip()
