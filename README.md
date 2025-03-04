---
![image](https://github.com/user-attachments/assets/fae68a0e-d1a7-43bb-8448-c4f5299763c6)

## **Notes App - Next.js + gRPC + SQLite**
A full-stack **Notes App** built with:
- **Next.js (TypeScript)**
- **Python gRPC Backend**
- **SQLite Database**
- **Tailwind CSS for Styling**

This application allows users to **create, read, update, and delete (CRUD) notes** via a modern UI.

---

## **📂 Project Structure**
```
nextjs-grpc-crud/
├── proto/                 # gRPC Protocol Buffers
│   └── notes.proto
├── server/                # Python gRPC Server
│   ├── server.py
│   ├── requirements.txt
│   ├── notes_pb2.py       # Generated from proto
│   ├── notes_pb2_grpc.py  # Generated from proto
│   └── notes.db           # SQLite Database (auto-created)
└── next-js-app/           # Next.js Frontend
    ├── src/
    │   ├── pages/
    │   │   ├── index.tsx        # Notes UI
    │   │   ├── api/
    │   │   │   ├── notes/
    │   │   │   │   ├── index.ts  # API for listing & creating notes
    │   │   │   │   ├── [id].ts   # API for updating & deleting notes
    ├── proto/notes.proto  # Copy of the proto file
    ├── styles/globals.css
    ├── package.json
    ├── tsconfig.json
    ├── tailwind.config.js
```

---

## **🛠 Installation**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/your-username/nextjs-grpc-notes-app.git
cd nextjs-grpc-notes-app
```

---

### **2️⃣ Set Up the Python gRPC Backend**
1. Navigate to the `server/` directory:
   ```bash
   cd server
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv env
   source env/bin/activate  # On Mac/Linux
   env\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Generate gRPC Python files from `.proto`:
   ```bash
   python -m grpc_tools.protoc -I../proto --python_out=. --grpc_python_out=. ../proto/notes.proto
   ```
5. Start the gRPC server:
   ```bash
   python server.py
   ```
   ✅ **You should see:** `Python gRPC server running on port 50051...`

---

### **3️⃣ Set Up the Next.js Frontend**
1. Open a new terminal and navigate to the `next-js-app/` directory:
   ```bash
   cd ../next-js-app
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
4. Open your browser and go to:
   ```
   http://localhost:3000
   ```
   ✅ **Your Notes App should be running! 🎉**

---

## **🚀 Features**
✅ **Create Notes** – Add a new note with a title and content.  
✅ **Read Notes** – Fetch and display all notes.  
✅ **Update Notes** – Edit an existing note.  
✅ **Delete Notes** – Remove unwanted notes.  
✅ **Modern UI** – Styled with Tailwind CSS.  
✅ **gRPC API** – Fast communication between Next.js and Python.  
✅ **SQLite Persistence** – Notes are saved locally.  

---

## **🔗 API Endpoints**
| Method | Endpoint        | Description                  |
|--------|---------------|------------------------------|
| **GET**  | `/api/notes`    | Fetch all notes              |
| **POST** | `/api/notes`    | Create a new note            |
| **GET**  | `/api/notes/:id` | Fetch a single note          |
| **PUT**  | `/api/notes/:id` | Update an existing note      |
| **DELETE** | `/api/notes/:id` | Delete a note               |

---

## **🐛 Troubleshooting**
### **1️⃣ Getting `500 Internal Server Error` while updating/deleting a note?**
- Ensure the **Python gRPC server is running** (`python server.py`).
- Check if the **note exists** in the database (`notes.db`).
- Look for errors in the server logs.

### **2️⃣ `notes.proto` file not found?**
- Ensure the `proto/notes.proto` file exists in the correct directory.
- If needed, modify the `PROTO_PATH` in `server.py` and API routes.

### **3️⃣ Getting `ECONNREFUSED` or gRPC connection issues?**
- Restart the gRPC server.
- Ensure the API routes point to `localhost:50051`.

### **4️⃣ Tailwind CSS not working?**
- Make sure Tailwind is installed and configured correctly.
- Restart the Next.js server (`npm run dev`).

---

## **📜 License**
This project is open-source and licensed under the **MIT License**.

---

## **💡 Contributing**
Contributions are welcome! Feel free to fork this repo, make changes, and submit a pull request.

---

## **🙌 Acknowledgments**
Thanks to:
- [Next.js](https://nextjs.org/)
- [gRPC](https://grpc.io/)
- [SQLite](https://www.sqlite.org/)
- [Tailwind CSS](https://tailwindcss.com/)

---

### 🎉 **Enjoy building with Next.js & gRPC! 🚀**
---
