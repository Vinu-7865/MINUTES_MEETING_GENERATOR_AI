import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from core.models import MeetingMinutesResult

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def process_meeting_transcript(transcript_text: str) -> MeetingMinutesResult:
    """
    Processes chaotic meeting text scripts into highly organized corporate summaries.
    """
    if not API_KEY:
        raise ValueError("Critical Security Error: GEMINI_API_KEY not found in local environment.")

    client = genai.Client(api_key=API_KEY)

    system_instruction = (
        "You are an elite corporate executive assistant and operational project manager. "
        "Your objective is to read disorganized, verbatim dialogue meeting transcripts and distill them "
        "into structured meeting minutes. You must extract clean bullet points, identify key players, "
        "track final decisions accurately, and isolate clear action items with deadlines. "
        "You must strictly return your response matching the requested JSON structure."
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"=== UNSTRUCTURED TRANSCRIPT ===\n{transcript_text}",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.1,  # Low temperature makes data extraction hyper-factual and precise
                response_mime_type="application/json",
                response_schema=MeetingMinutesResult,
            ),
        )
        
        return MeetingMinutesResult.model_validate_json(response.text)

    except Exception as e:
        raise RuntimeError(f"Gemini Processing Pipeline Failed: {str(e)}")