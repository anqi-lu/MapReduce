base_path = 'docs/'
files = glob.glob(base_path + '*.txt')
  inverted_indexes = {}
  
  for i, file_name in enumerate(files):
    with open(file_name, 'r') as f:
      read_data = f.read()
      local_file_name = file_name[len(base_path):]

      self._documents.append(local_file_name)
      f.close()
    