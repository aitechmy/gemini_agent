import time
from google import genai

class PDFHandler:
    def __init__(self, client: genai.Client):
        self.client = client

    def upload_and_wait(self, file_path):
        """Uploads a PDF and waits for Google to finish processing it."""
        print(f"🔄 Uploading: {file_path.name}...")
        
        # Upload the file
        uploaded_file = self.client.files.upload(file=str(file_path))
        
        # Check status (Active means it's ready to be read)
        while uploaded_file.state.name == "PROCESSING":
            print("...still processing...")
            time.sleep(2)
            uploaded_file = self.client.files.get(name=uploaded_file.name)
            
        print(f"✅ {file_path.name} is active.")
        return uploaded_file