from sqlalshemy.engine import create_engine
from sqlalshemy.orm import Session

class Database:
    def __init__(self):
        self.engien = create_engine("postgresql://postgres:123456@localhost/ttt")
        self.session = Session(self.session)