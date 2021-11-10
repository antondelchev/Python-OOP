class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, c1):
        pass

    def add_topic(self, t1):
        pass

    def add_document(self, d1):
        pass

    def edit_category(self, category_id: int, new_name: str):
        pass

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        pass

    def edit_document(self, document_id: int, new_file_name: str):
        pass

    def delete_category(self, category_id):
        pass

    def delete_topic(self, topic_id):
        pass

    def delete_document(self, document_id):
        pass

    def get_document(self, param):
        pass

    def __repr__(self):
        pass
