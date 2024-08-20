import os
import requests

class BulkUpdateUploader:
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.upload_url = f"{self.base_url}/api/bulk-update/"  # Update to the correct API endpoint

        # Paths to sample files for testing
        self.excel_file_path = os.path.join(os.path.dirname(__file__), 'sample_data.xlsx')
        self.packages_file_path = os.path.join(os.path.dirname(__file__), 'sample_packages.xlsx')

    def upload_only_excel_file(self):
        with open(self.excel_file_path, 'rb') as excel_file:
            files = {'excel_file': excel_file}
            response = requests.post(self.upload_url, files=files)
            self._handle_response(response)

    def upload_excel_and_packages_file(self):
        with open(self.excel_file_path, 'rb') as excel_file, open(self.packages_file_path, 'rb') as packages_file:
            files = {'excel_file': excel_file, 'packages_file': packages_file}
            response = requests.post(self.upload_url, files=files)
            self._handle_response(response)

    def upload_without_excel_file(self):
        response = requests.post(self.upload_url, files={})
        self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 201:
            print("Success: ", response.json())
        else:
            print(f"Failed with status code {response.status_code}: ", response.json())

if __name__ == '__main__':
    base_url = 'http://localhost:8000'  # Replace with your actual base URL
    uploader = BulkUpdateUploader(base_url)

    print("Uploading only Excel file:")
    uploader.upload_only_excel_file()

    print("\nUploading Excel file and packages file:")
    uploader.upload_excel_and_packages_file()

    print("\nUploading without Excel file:")
    uploader.upload_without_excel_file()
