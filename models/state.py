#!/usr/bin/python3
"""Define state representation"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a State.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
