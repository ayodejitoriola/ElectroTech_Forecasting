#import image
FROM python:3.9-slim
#create a working folder
WORKDIR /app
#copy requirement.txt
COPY requirements.txt .
#install environment
RUN pip install --no-cache-dir -r requirements.txt
#copy all file into work directory
COPY . .
#expose on a particular port
EXPOSE 8501
#run CMD
CMD ["streamlit","run", "inference.py"]
