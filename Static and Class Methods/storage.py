from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for el in self.categories:
            if el.name == category.name:
                return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for el in self.topics:
            if el.topic == topic.topic:
                return
        self.topics.append(topic)

    def add_document(self, document: Document):
        for el in self.documents:
            if el.file_name == document.file_name:
                return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for el in self.categories:
            if el.id == category_id:
                el.name = new_name
                return

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for el in self.topics:
            if el.id == topic_id:
                el.topic = new_topic
                el.storage_folder = new_storage_folder
                return

    def edit_document(self, document_id: int, new_file_name: str):
        for el in self.documents:
            if el.id == document_id:
                el.file_name = new_file_name
                return

    def delete_category(self, category_id):
        for el in self.categories:
            if el.id == category_id:
                self.categories.remove(el)
                return

    def delete_topic(self, topic_id):
        for el in self.topics:
            if el.id == topic_id:
                self.topics.remove(el)
                return

    def delete_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                self.documents.remove(el)
                return

    def get_document(self, document_id):
        for el in self.documents:
            if el.id == document_id:
                return str(el)

    def __repr__(self):
        result = "\n".join([str(x) for x in self.documents])
        return result
