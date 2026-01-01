from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict

# Define runtime context schema
@dataclass
class RuntimeContext:
    """Custom runtime context schema."""
    user_id: str


@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # manager response (always required)
    manager_response: str
    # Any interesting information about the warehouse if available
    warehouse_conditions: str | None = None

@dataclass
class ClaudeHaikuConfig:
    # Model name to use.
    model_name: str = 'Jane Doe'
    # A non-negative float that tunes the degree of randomness in generation
    temperature: float | None = 0
    # Total probability mass of tokens to consider at each step
    top_p: float
    # Number of retries allowed for requests sent to the Claude API
    max_retries: int = 2
    max_tokens: int
    timeout: int | None
    max_retries: int
    # The type of output this Runnable produces specified as a Pydantic model
    input_schema: type[BaseModel]
