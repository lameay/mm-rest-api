from sqlalchemy import Column, String, Integer
from database import Base

class FileUpload(Base):
    __table__name__ = "fileUploads"
    id = Column(Integer, primary_key=True)
    file_name = Column(String(50), unique=False)
    word_count = Column(Integer, unique=False)

    def __init__(self, file_name=None, word_count=None):
        self.file_name = file_name
        self.word_count = word_count


    def __repr__(self):
        return '<FileUpload %r>' % (self.file_name)


