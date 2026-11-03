
import { useState } from 'react'
import { FileText, Upload, X, LoaderCircle } from 'lucide-react'
import { previewDocument } from '../../services/api'

const MAX_FILE_SIZE = 10 * 1024 * 1024

function DocumentUploader() {
  const [loading, setLoading] = useState(false)
  const [preview, setPreview] = useState(null)
  const [error, setError] = useState('')
  const [selectedFile, setSelectedFile] = useState(null)

  async function handleFileChange(event) {
    const file = event.target.files?.[0]

    if (!file) return

    setError('')
    setPreview(null)

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

  function clearPreview() {
    setSelectedFile(null)
    setPreview(null)
    setError('')

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
            Review the extracted text. It has not been saved to your assignments.
          </p>
        </div>
      )}
    </section>
  )
}

export default DocumentUploader
