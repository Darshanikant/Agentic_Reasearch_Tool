# main.py

from utils.search import search_web
from utils.summarizer import summarize_results
from utils.pdf_writer import save_summary_to_pdf

def main():
    print("🔍 Welcome to the Agentic Research Bot!")
    topic = input("Enter a topic to research: ").strip()

    print(f"\n📡 Searching web for: {topic}")
    results = search_web(topic)
    
    if not results:
        print("❌ No results found.")
        return

    print("\n🧠 Summarizing the findings with Gemini...")
    summary = summarize_results(results)

    print("\n📄 Saving the summary to a PDF...")
    pdf_path = save_summary_to_pdf(topic, summary)

    print(f"\n✅ Report generated successfully: {pdf_path}")

if __name__ == "__main__":
    main()
