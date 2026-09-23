import traceback
import nbformat
import nbclient

path = r"c:\Users\rehan\Desktop\Kaam\Oasis Infobyte Data Analytics\Level-1 Task-1\Retail_Sales_EDA .ipynb"
nb = nbformat.read(path, as_version=4)
client = nbclient.NotebookClient(nb, timeout=180, kernel_name='python3')
try:
    client.execute()
    print('NOTEBOOK_EXECUTION: SUCCESS')
except Exception as e:
    print('NOTEBOOK_EXECUTION: FAILED')
    print(type(e).__name__, e)
    traceback.print_exc()
    raise
