
import { useState } from 'react'
import { FileText, Upload, X, LoaderCircle } from 'lucide-react'
import {
  previewDocument,
  extractAssignmentDetails,
} from '../../services/api'

const MAX_FILE_SIZE = 10 * 1024 * 1024

function DocumentUploader({ onCreateAssignment }) {
  const [loading, setLoading] = useState(false)
  const [preview, setPreview] = useState(null)
  const [error, setError] = useState('')
  const [selectedFile, setSelectedFile] = useState(null)
  const [aiLoading, setAiLoading] = useState(false)
  const [aiSuggestions, setAiSuggestions] = useState(null)
  const [aiError, setAiError] = useState('')
  const [saving, setSaving] = useState(false)
  const [saveError, setSaveError] = useState('')

  async function handleFileChange(event) {
    const file = event.target.files?.[0]

    if (!file) return

    setError('')
    setPreview(null)
    setAiSuggestions(null)
    setAiError('')
    setSaveError('')
    setSelectedFile(null)

    if (!file.name.toLowerCase().endsWith('.pdf')) {
      setError('Please select a PDF file.')
      setSelectedFile(null)
      event.target.value = ''
      return
    }

    if (file.size === 0) {
      setError('The selected file is empty.')
      setSelectedFile(null)
      event.target.value = ''
      return
    }

    if (file.size > MAX_FILE_SIZE) {
      setError('The PDF must be smaller than 10 MB.')
      setSelectedFile(null)
      event.target.value = ''
      return
    }

    setSelectedFile(file)
    setLoading(true)

    try {
      const result = await previewDocument(file)
      setPreview(result)
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        'Unable to extract text from this PDF. Please try another file.'
      )
    } finally {
      setLoading(false)
    }
  }

  async function handleAIExtraction() {
    if (!preview?.text) return

    setAiLoading(true)
    setAiError('')
    setAiSuggestions(null)

    try {
      const result = await extractAssignmentDetails(preview.text)

      setAiSuggestions({
        title: result.title || '',
        due_date: result.due_date || '',
        requirements: result.requirements || [],
      })
    } catch (err) {
      setAiError(
        err.response?.data?.detail ||
        'AI extraction failed. Make sure Ollama is running and try again.'
      )
    } finally {
      setAiLoading(false)
    }
  }

  async function handleConfirmAndSave() {
  if (!aiSuggestions?.title.trim()) {
    setSaveError('Please enter an assignment title.')
    return
  }

  setSaving(true)
  setSaveError('')

  const requirementsText = aiSuggestions.requirements
    .map((item) => `- ${item}`)
    .join('\n')

  const description = requirementsText
    ? `Requirements:\n${requirementsText}`
    : null

  try {
    const success = await onCreateAssignment({
      title: aiSuggestions.title.trim(),
      description,
      due_date: aiSuggestions.due_date || null,
      status: 'pending',
      priority: 'medium',
    })

    if (success) {
      clearPreview()
    } else {
      setSaveError('Assignment could not be saved. Please try again.')
    }
  } catch {
    setSaveError('An unexpected error occurred while saving.')
  } finally {
    setSaving(false)
  }
}

  function clearPreview() {
    setSelectedFile(null)
    setPreview(null)
    setError('')
    setAiSuggestions(null)
    setAiError('')
    setSaveError('')

    const fileInput = document.getElementById('document-upload')
    if (fileInput) fileInput.value = ''
  }

  return (
    <section className="document-uploader">
      <div className="document-uploader-header">
        <div>
          <h2>Import assignment document</h2>
          <p>
            Upload a PDF to extract its text for review.
            Nothing will be saved as an assignment.
          </p>
        </div>

        <FileText size={24} />
      </div>

      <label
        htmlFor="document-upload"
        className="document-upload-button"
      >
        <Upload size={17} />
        Choose PDF
      </label>

      <input
        id="document-upload"
        type="file"
        accept=".pdf,application/pdf"
        onChange={handleFileChange}
        disabled={loading}
        hidden
      />

      {selectedFile && (
        <div className="document-selected-file">
          <FileText size={17} />
          <span>{selectedFile.name}</span>
        </div>
      )}

      {loading && (
        <div className="document-loading" role="status">
          <LoaderCircle className="loading-spinner" size={20} />
          Extracting PDF text...
        </div>
      )}

      {error && (
        <div className="document-error" role="alert">
          {error}
        </div>
      )}

      {preview && (
        <div className="document-preview">
          <div className="document-preview-header">
            <div>
              <h3>Extracted text</h3>
              <p>
                {preview.character_count.toLocaleString()} characters extracted
              </p>
            </div>

            <button
              type="button"
              className="document-clear-button"
              onClick={clearPreview}
              aria-label="Clear document preview"
            >
              <X size={18} />
            </button>
          </div>

          {preview.text ? (
            <pre className="document-preview-text">
              {preview.text}
            </pre>
          ) : (
            <p className="document-empty-preview">
              No text was extracted from this document.
            </p>
          )}

          <p className="document-preview-note">
                      <button
            type="button"
            className="document-upload-button"
            onClick={handleAIExtraction}
            disabled={aiLoading || !preview.text}
          >
            {aiLoading ? (
              <>
                <LoaderCircle className="loading-spinner" size={17} />
                Analysing with AI...
              </>
            ) : (
              'Extract assignment details with AI'
            )}
          </button>

          {aiError && (
            <div className="document-error" role="alert">
              {aiError}
            </div>
            )}

                    {aiSuggestions && (
            <div className="ai-review-section">
              <h3>Review AI suggestions</h3>
              <p>
                Check and correct these details before saving your assignment.
              </p>

              <label htmlFor="ai-title">Assignment title</label>
              <input
                id="ai-title"
                type="text"
                maxLength={200}
                value={aiSuggestions.title}
                onChange={(event) =>
                  setAiSuggestions((current) => ({
                    ...current,
                    title: event.target.value,
                  }))
                }
                placeholder="Assignment title"
              />

              <label htmlFor="ai-due-date">Due date</label>
              <input
                id="ai-due-date"
                type="date"
                value={aiSuggestions.due_date}
                onChange={(event) =>
                  setAiSuggestions((current) => ({
                    ...current,
                    due_date: event.target.value,
                  }))
                }
              />

              <label htmlFor="ai-requirements">Requirements</label>
              <textarea
                id="ai-requirements"
                rows={5}
                value={aiSuggestions.requirements.join('\n')}
                onChange={(event) =>
                  setAiSuggestions((current) => ({
                    ...current,
                    requirements: event.target.value
                      .split('\n')
                      .map((item) => item.trim())
                      .filter(Boolean),
                  }))
                }
                placeholder="One requirement per line"
              />

              <p className="document-preview-note">
                AI-generated details may be inaccurate. Review everything before saving.
              </p>
              {saveError && (
  <div className="document-error" role="alert">
    {saveError}
  </div>
)}

<div className="ai-review-actions">
  <button
    type="button"
    className="document-clear-button"
    onClick={() => setAiSuggestions(null)}
    disabled={saving}
  >
    Discard suggestions
  </button>

  <button
    type="button"
    className="document-upload-button"
    onClick={handleConfirmAndSave}
    disabled={saving || !aiSuggestions.title.trim()}
  >
    {saving ? (
      <>
        <LoaderCircle className="loading-spinner" size={17} />
        Saving...
      </>
    ) : (
      'Confirm & Save Assignment'
    )}
  </button>
</div>

            </div>
          )}
            Review the extracted text. It has not been saved to your assignments.
          </p>
        </div>
      )}
    </section>
  )
}

export default DocumentUploader
