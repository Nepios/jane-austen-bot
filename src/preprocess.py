
import nltk
# Set a specific directory for NLTK data
# nltk_data_dir = os.path.expanduser('~/nltk_data')
# if not os.path.exists(nltk_data_dir):
#     os.makedirs(nltk_data_dir)

# nltk.data.path.append(nltk_data_dir)
# nltk.download('punkt', download_dir=nltk_data_dir)

# print("Current working directory:", os.getcwd())
with open('data/raw_texts/emma.txt', encoding='utf-8') as f:
    austen_text = f.read()
sentences = nltk.sent_tokenize(austen_text)
print(sentences[:10])  # Preview Austen sentences