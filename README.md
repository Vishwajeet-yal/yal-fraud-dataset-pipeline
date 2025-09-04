# YAL.ai Fraud Dataset Pipeline

Project Overview
The goal of this project is to collect, clean, annotate, and structure fraud-related conversations from real platforms like Reddit and Telegram.  
This dataset will serve as the foundation for building scalable AI fraud detection systems.

Repository Structure
- `data_collector.py` → Python script to scrape data from Reddit and Telegram  
- `collected_data.csv` → Final dataset with annotations (fraud categories)  
- `report.pdf` → Documentation with introduction, ethics, methodology, and references  
- `requirements.txt` → List of dependencies to run the project  
- `README.md` → Project documentation  

Setup Instructions

1. Clone this repository:
   ```bash
   git clone https://github.com/Vishwajeet-yal/yal-fraud-dataset-pipeline.git
   cd yal-fraud-dataset-pipeline

2. Install dependencies:

pip install -r requirements.txt


3. Run the scraper:

python3 data_collector.py

