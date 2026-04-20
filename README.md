# 🧠 AI PDF Editor (HUGGING FACE)

An intelligent PDF editing tool powered by Hugging Face Transformers.
This application allows users to upload a PDF, edit its content, apply AI-based transformations, and download the updated document.

---

## 🚀 Features

* 📄 Upload and extract text from PDF files
* ✏️ Edit full document content directly
* 🤖 AI-powered text operations:

  * Summarization
  * Paraphrasing
  * Grammar Correction
* 💾 Export edited content back into PDF format

---

## 🧠 Tech Stack

* Python
* Streamlit (UI)
* PyMuPDF (PDF processing)
* Hugging Face Transformers (NLP models)

---

## 📁 Project Structure

```
ai-pdf-editor/
│
├── app.py
├── core/
│   ├── nlp_engine.py
│   ├── pdf_editor.py
│
├── sample_pdf.pdf
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-pdf-editor.git
cd ai-pdf-editor
```

2. Create virtual environment (recommended):

```
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 🧪 How to Use

1. Upload a PDF file
2. The text will be extracted and displayed
3. Edit the text manually OR use AI buttons:

   * **Summarize**
   * **Paraphrase**
   * **Correct**
4. Click **Save PDF**
5. Download the edited document

---

## ⚠️ Limitations

* Layout and formatting may not be perfectly preserved
* Works best with text-based PDFs (not scanned documents)
* Complex structures (tables, multi-column layouts) may not render accurately

---

## 🔮 Future Improvements

* Support for scanned PDFs using OCR
* Section-wise editing instead of full document
* Chat-based AI editing (prompt-driven editing)
* Deployment on Hugging Face Spaces

---

## 👨‍💻 Author

Developed as an NLP project using Hugging Face models and PDF processing techniques.

---

## 📜 License

This project is open-source and available under the MIT License.
