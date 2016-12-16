class FeedType:
    def __init__(self, id, type):
        self.id = id
        self.type=type

def insert_feedtype(cursor,feedtype):
    statement = """INSERT INTO FEEDTYPES (ID,TYPE) VALUES (
                %s, %s
                )"""
    cursor.execute(statement,(feedtype.id,feed.feedtype));
def get_feedtype_by_id(cursor,id):
    statement = """SELECT TYPE FROM FEEDTYPE WHERE (ID = %(id)s)"""
    cursor.execute(statement,{'id':id});
