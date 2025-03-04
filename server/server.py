import sqlite3
from concurrent import futures
import grpc
import notes_pb2
import notes_pb2_grpc

DATABASE = "notes.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class NoteService(notes_pb2_grpc.NoteServiceServicer):
    def CreateNote(self, request, context):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (request.title, request.content))
        conn.commit()
        note_id = c.lastrowid
        conn.close()
        return notes_pb2.NoteResponse(note=notes_pb2.Note(id=note_id, title=request.title, content=request.content))

    def GetNote(self, request, context):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("SELECT id, title, content FROM notes WHERE id = ?", (request.id,))
        row = c.fetchone()
        conn.close()
        if row:
            return notes_pb2.NoteResponse(note=notes_pb2.Note(id=row[0], title=row[1], content=row[2]))
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Note not found")
        return notes_pb2.NoteResponse()

    def ListNotes(self, request, context):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("SELECT id, title, content FROM notes")
        rows = c.fetchall()
        conn.close()
        notes = [notes_pb2.Note(id=row[0], title=row[1], content=row[2]) for row in rows]
        return notes_pb2.ListNotesResponse(notes=notes)

    def UpdateNote(self, request, context):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (request.title, request.content, request.id))
        conn.commit()
        if c.rowcount == 0:
            conn.close()
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Note not found")
            return notes_pb2.NoteResponse()
        conn.close()
        return notes_pb2.NoteResponse(note=notes_pb2.Note(id=request.id, title=request.title, content=request.content))

    def DeleteNote(self, request, context):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute("DELETE FROM notes WHERE id = ?", (request.id,))
        conn.commit()
        success = c.rowcount > 0
        conn.close()
        return notes_pb2.DeleteNoteResponse(success=success)

def serve():
    init_db()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notes_pb2_grpc.add_NoteServiceServicer_to_server(NoteService(), server)
    server.add_insecure_port('[::]:50051')
    print("Python gRPC server running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
