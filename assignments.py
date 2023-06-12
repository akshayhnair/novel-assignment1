from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import DirectoryLoader
import os
import nltk
import magic
os.environ["OPENAI_API_KEY"]="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"
loader = DirectoryLoader('/content/sample_data/files', glob='**/*.txt')
docs =loader.load()
char_text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
doc_texts = char_text_splitter.split_documents(docs)
openAI_embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
vStore =Chroma.from_documents(doc_texts,openAI_embeddings)
model =VectorDBQA.from_chain_type(llm=OpenAI(),chain_type="stuff",vectorstore=vStore)
question ="what are the effects of homelessness?"
model.run(question)
model =VectorDBQA.from_chain_type(llm=OpenAI(),chain_type="stuff",vectorstore=vStore, return_source_documents=True)
question="what are causes of homelesness?"
response=model({"query":question})
response['source_documents']
