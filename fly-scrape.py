import os
import sys
import json
import asyncio
import requests
from xml.etree import ElementTree
from typing import List, Dict, Any
from dataclasses import dataclass
from datetime import datetime, timezone
from urllib.parse import urlparse
from dotenv import load_dotenv  

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from openai import AsyncOpenAI
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize Supabase and OpenAI clients
supabase: Client = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")  

# ... (rest of original content) 