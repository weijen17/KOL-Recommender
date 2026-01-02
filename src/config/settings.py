"""Configuration settings for the two-agent system"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application settings"""

    # Paths
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    RESULT_DIR: Path = BASE_DIR / "artifact/result"
    INPUT_DIR: Path = BASE_DIR / "input/raw_data"
    LOG_DIR: Path = BASE_DIR / "logs"

    # Input
    INPUT_FILENAME: str = os.getenv("INPUT_FILENAME", "KOL_Listing.xlsx")
    INPUT_NAME: Path = INPUT_DIR / INPUT_FILENAME

    # Output
    OUTPUT_RESULT_NAME: str = os.getenv("OUTPUT_RESULT_NAME", "KOL_Recommender_Result.xlsx")
    RESULT_NAME: Path = RESULT_DIR / OUTPUT_RESULT_NAME

    TOP_N: int = os.getenv("TOP_N", 50)

    def __init__(self):
        """Initialize settings and create necessary directories"""
        self.RESULT_DIR.mkdir(exist_ok=True)
        self.LOG_DIR.mkdir(exist_ok=True)

settings = Settings()

