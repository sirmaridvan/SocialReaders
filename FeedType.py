class FeedType:
    def __init__(self, id, type):
        self.id = id
        self.type=type

def insert_feedtype(cursor,feedtype):
    statement = """INSERT INTO FEEDTYPES (ID,TYPE) VALUES (
                %s, %s
                )"""
    cursor.execute(statement,(feedtype.id,feed.feedtype));
