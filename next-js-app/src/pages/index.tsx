"use client"

import type React from "react"
import { useEffect, useState, useCallback } from "react"

interface Note {
  id: number
  title: string
  content: string
}

interface FormData {
  title: string
  content: string
}

const Home: React.FC = () => {
  const [notes, setNotes] = useState<Note[]>([])
  const [form, setForm] = useState<FormData>({ title: "", content: "" })
  const [editing, setEditing] = useState<number | null>(null)

  const fetchNotes = useCallback(async (): Promise<void> => {
    const res = await fetch("/api/notes")
    const data = await res.json()
    setNotes(data)
  }, [])

  useEffect(() => {
    fetchNotes()
  }, [fetchNotes])

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault()
    if (editing !== null) {
      await fetch(`/api/notes/${editing}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      })
      setEditing(null)
    } else {
      await fetch("/api/notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      })
    }
    setForm({ title: "", content: "" })
    fetchNotes()
  }

  const handleDelete = async (id: number): Promise<void> => {
    await fetch(`/api/notes/${id}`, { method: "DELETE" })
    fetchNotes()
  }

  const startEdit = (note: Note): void => {
    setEditing(note.id)
    setForm({ title: note.title, content: note.content })
  }

  return (
    <div className="min-h-screen bg-slate-900 text-white p-4 md:p-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="font-extrabold text-3xl md:text-4xl text-cyan-500 mb-8 text-center"><span className="text-white">Notes</span> App</h1>

        <div className="bg-slate-800 rounded-lg p-6 mb-8 shadow-lg">
          <h2 className="text-xl font-bold mb-4 text-cyan-400">{editing !== null ? "Edit Note" : "Create New Note"}</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="flex flex-col gap-4">
              <input
                type="text"
                placeholder="Title"
                value={form.title}
                onChange={(e) => setForm({ ...form, title: e.target.value })}
                required
                className="w-full px-4 py-2 bg-slate-700 rounded-md border border-slate-600 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
              />
              <textarea
                placeholder="Content"
                value={form.content}
                onChange={(e) => setForm({ ...form, content: e.target.value })}
                required
                rows={4}
                className="w-full px-4 py-2 bg-slate-700 rounded-md border border-slate-600 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent resize-none"
              />
            </div>
            <div className="flex justify-end">
              {editing !== null && (
                <button
                  type="button"
                  onClick={() => {
                    setEditing(null)
                    setForm({ title: "", content: "" })
                  }}
                  className="px-4 py-2 mr-2 bg-slate-700 hover:bg-slate-600 rounded-md transition-colors"
                >
                  Cancel
                </button>
              )}
              <button
                type="submit"
                className="px-4 py-2 bg-cyan-600 hover:bg-cyan-500 rounded-md font-medium transition-colors"
              >
                {editing !== null ? "Update Note" : "Add Note"}
              </button>
            </div>
          </form>
        </div>

        <div className="bg-slate-800 rounded-lg p-6 shadow-lg">
          <h2 className="text-xl font-bold mb-4 text-cyan-400">Your Notes</h2>
          {notes.length === 0 ? (
            <p className="text-slate-400 text-center py-6">No notes yet. Create one to get started!</p>
          ) : (
            <ul className="space-y-4">
              {notes.map((note) => (
                <li key={note.id} className="bg-slate-700 rounded-lg p-4 shadow transition-all hover:shadow-md">
                  <div className="flex flex-col">
                    <h3 className="font-bold text-lg text-cyan-300 mb-2">{note.title}</h3>
                    <p className="text-slate-300 whitespace-pre-wrap mb-3">{note.content}</p>
                    <div className="flex justify-end space-x-2 mt-2">
                      <button
                        onClick={() => startEdit(note)}
                        className="p-2 text-sm bg-slate-600 hover:bg-slate-500 rounded transition-colors"
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => handleDelete(note.id)}
                        className="p-2 text-sm bg-red-700 hover:bg-red-600 rounded transition-colors"
                      >
                        Delete
                      </button>
                    </div>
                  </div>
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </div>
  )
}

export default Home

