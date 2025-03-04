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
  if (req.method === 'GET') {
  
    client.ListNotes({}, (err: any, response: any) => {
      if (err) {
        res.status(500).json({ error: err.message });
      } else {
        res.status(200).json(response.notes);
      }
    });
  } else if (req.method === 'POST') {
    const { title, content } = req.body;
    client.CreateNote({ title, content }, (err: any, response: any) => {
      if (err) {
        res.status(500).json({ error: err.message });
      } else {
        res.status(201).json(response.note);
      }
    });
  } else {
    res.status(405).end(); 
  }
}
