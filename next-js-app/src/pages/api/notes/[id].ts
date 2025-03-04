import { NextApiRequest, NextApiResponse } from 'next';
import * as grpc from '@grpc/grpc-js';
import * as protoLoader from '@grpc/proto-loader';
import path from 'path';

const PROTO_PATH = path.join(process.cwd(), 'proto', 'notes.proto');

const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

const notesProto = grpc.loadPackageDefinition(packageDefinition).notes;
const client = new notesProto.NoteService(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { id } = req.query;
  const noteId = Number(id);

  if (req.method === 'GET') {
    client.GetNote({ id: noteId }, (err: any, response: any) => {
      if (err) {
        res.status(500).json({ error: err.message });
      } else {
        res.status(200).json(response.note);
      }
    });
  } else if (req.method === 'PUT') {
    const { title, content } = req.body;
    client.UpdateNote({ id: noteId, title, content }, (err: any, response: any) => {
      if (err) {
        res.status(500).json({ error: err.message });
      } else {
        res.status(200).json(response.note);
      }
    });
  } else if (req.method === 'DELETE') {
    client.DeleteNote({ id: noteId }, (err: any, response: any) => {
      if (err) {
        res.status(500).json({ error: err.message });
      } else {
        res.status(200).json({ success: response.success });
      }
    });
  } else {
    res.status(405).end(); 
  }
}
