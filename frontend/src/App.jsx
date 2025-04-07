import { useState } from 'react'
import './App.css'

function App() {
  const [question, setQuestion] = useState('')
  const [answer, setAnswer] = useState('')

  const askQuestion = async () => {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    })
    const data = await res.json()
    setAnswer(data.answer)
  }

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">CS Visualizer</h1>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="w-full border p-2 mb-2"
        rows="4"
        placeholder="Ask a computer science question..."
      />
      <button
        onClick={askQuestion}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        Ask
      </button>
      {answer && (
        <div className="mt-4 p-4 border rounded bg-gray-100">
          <h2 className="font-semibold">Answer:</h2>
          <p>{answer}</p>
        </div>
      )}
    </div>
  )
}

export default App
