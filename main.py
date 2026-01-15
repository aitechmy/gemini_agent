import time
from google import genai
from config import Config
from src.pdf_handler import PDFHandler
from src.researcher import ResearchAgent

def main():
    cfg = Config()
    client = genai.Client(api_key=cfg.API_KEY)
    
    handler = PDFHandler(client)
    agent = ResearchAgent(client, cfg)

    # 1. Scan the folder
    pdf_files = list(cfg.LIT_DIR.glob("*.pdf"))
    print(f"📚 Found {len(pdf_files)} papers in 'literature/' folder.")

    for pdf in pdf_files:
        try:
            # 2. Upload
            file_obj = handler.upload_and_wait(pdf)
            
            # 3. Analyze with Thinking Budget
            print(f"🧠 Agent is thinking and mining data from {pdf.name}...")
            analysis_md = agent.analyze_paper(file_obj)
            
            # 4. Save Output
            output_name = cfg.OUTPUT_DIR / f"Analysis_{pdf.stem}.md"
            with open(output_name, "w", encoding="utf-8") as f:
                f.write(analysis_md)
            
            print(f"💾 Saved analysis to {output_name}")

            # 5. Rate Limit Protection (Free Tier)
            print(f"⏳ Waiting {cfg.RPM_DELAY}s to protect API quota...")
            time.sleep(cfg.RPM_DELAY)

        except Exception as e:
            print(f"❌ Error processing {pdf.name}: {e}")

if __name__ == "__main__":
    main()