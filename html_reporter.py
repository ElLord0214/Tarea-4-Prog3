class HtmlReporter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.report_file = open(file_name, 'w', encoding='utf-8')
        self.report_file.write('<html><head><meta charset="UTF-8"><title>Reporte de prueba</title></head><body>')
    
    def add_info(self, message):
        self.report_file.write(f'<p>{message}</p>')
        
    def close(self):
        self.report_file.write('</body></html>')
        self.report_file.close()


