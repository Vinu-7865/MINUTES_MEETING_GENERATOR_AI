from pydantic import BaseModel, Field
from typing import List, Optional

class ActionItem(BaseModel):
    """Schema representing an explicitly assigned project task."""
    task: str = Field(description="The exact description of the work that needs to be done.")
    assignee: str = Field(description="The name of the individual or team responsible. Use 'Unassigned' if unknown.")
    deadline: str = Field(description="The specified timeline or date mentioned. Use 'None specified' if missing.")

class MeetingMinutesResult(BaseModel):
    """The master schema mapping directly to our corporate dashboard layouts."""
    executive_summary: str = Field(description="A highly concise, 3-4 sentence high-level overview of the meeting's core objective.")
    participants: List[str] = Field(description="List of detected names or titles of individuals speaking/presenting.")
    key_discussion_points: List[str] = Field(description="Major talking points, updates, or arguments brought up during the session.")
    final_decisions: List[str] = Field(description="Concrete decisions, approvals, or conclusions reached by the group.")
    action_checklist: List[ActionItem] = Field(description="A structured roadmap of tasks assigned to participants with clear deadlines.")