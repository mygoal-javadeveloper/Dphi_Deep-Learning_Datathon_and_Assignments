def upload_videofiles():
  from google.colab import files
  uploaded_files = files.upload()
  for k, v in uploaded_files.items():
    #opens the uploaded files in write and binary mode. Binary mode for images
    open(k, 'wb').write(v)
  return list(uploaded_files.keys())

frames = upload_videofiles() #select all video frames from the folder (dataset)