from typing import Optional

from dotenv import load_dotenv
from langchain.pydantic_v1 import BaseSettings
from langchain.schema import SystemMessage

from codeinterpreterapi.prompts import code_interpreter_system_message

# .env file
load_dotenv(dotenv_path="./.env")


class CodeInterpreterAPISettings(BaseSettings):
    """
    CodeInterpreter API Config
    """

    DEBUG: bool = False

    # Models
    OPENAI_API_KEY: Optional[str] = None
    AZURE_API_KEY: Optional[str] = None
    AZURE_API_BASE: Optional[str] = None
    AZURE_API_VERSION: Optional[str] = None
    AZURE_DEPLOYMENT_NAME: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    OPENROUTER_API_KEY: Optional[str] = None
    OPENROUTER_API_BASE: Optional[str] = "https://openrouter.ai/api/v1"
    OPENROUTER_DEFAULT_CHAT_MODEL = "openai/gpt-4"

    # LLM Settings
    MODEL: str = "gpt-3.5-turbo"
    TEMPERATURE: float = 0.02
    DETAILED_ERROR: bool = True
    SYSTEM_MESSAGE: SystemMessage = code_interpreter_system_message
    REQUEST_TIMEOUT: int = 3 * 60
    MAX_ITERATIONS: int = 15
    MAX_RETRY: int = 3

    # Production Settings
    HISTORY_BACKEND: Optional[str] = None
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = "postgresql://postgres:postgres@localhost:5432/postgres"

    # CodeBox
    CODEBOX_API_KEY: Optional[str] = None
    CUSTOM_PACKAGES: list[str] = []  # implement custom logic for codebox

    # deprecated
    VERBOSE: bool = DEBUG


settings = CodeInterpreterAPISettings()
