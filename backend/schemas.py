from typing import List, Optional

from pydantic import BaseModel

class TicketBase(BaseModel):
    title: str
    contact: str
    description: str
    solution: str
    resolved: bool
    data: str
    description: Optional[str] = None

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int
    resolved_by_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    resolved_tickets: List[Ticket] = []

    class Config:
        orm_mode = True


