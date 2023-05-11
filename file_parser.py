import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []

MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []

AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []

DOC_DOCS = []
DOCX_DOCS = []
TXT_DOCS = []
PDF_DOCS = []
XLSX_DOCS = []
PPTX_DOCS = []

ZIP_ARCH = []
GZ_ARCH = []
TAR_ARCH = []
 
MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'ZIP': ZIP_ARCH,
    'GZ': GZ_ARCH,
    'TAR': TAR_ARCH,
    'DOC': DOC_DOCS,
    'DOCX': DOCX_DOCS,
    'TXT': TXT_DOCS,
    'PDF': PDF_DOCS,
    'XLSX': XLSX_DOCS,
    'PPTX': PPTX_DOCS    
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        # Робота з папкою
        if item.is_dir():
            # Перевіряємо, щоб папка не була тією в яку ми вже складаємо файли.
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images'):
                FOLDERS.append(item)
                scan(item)  # скануємо цю вкладену папку - рекурсія
            continue  # переходимо до наступного елемента в сканованій папці
        # else:
        # Робота з файлом
        ext = get_extension(item.name)  # беремо розширення файлу
        full_name = folder / item.name  # беремо повний шлях до файлу
        if not ext:
            MY_OTHER.append(full_name)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSIONS.add(ext)
                container.append(full_name)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder: {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f"Images jpeg: {JPEG_IMAGES}")
    print(f"Images jpg: {JPG_IMAGES}")
    print(f"Images png: {PNG_IMAGES}")
    print(f"Images svg: {SVG_IMAGES}")
    print(f"Audio mp3: {MP3_AUDIO}")    
    print(f"Audio ogg: {OGG_AUDIO}")    
    print(f"Audio wav: {WAV_AUDIO}")    
    print(f"Audio amr: {AMR_AUDIO}")    
    print(f"Video avi: {AVI_VIDEO}")    
    print(f"Video mp4: {MP4_VIDEO}")    
    print(f"Video mov: {MOV_VIDEO}")    
    print(f"Video mkv: {MKV_VIDEO}")    
    print(f"Archives zip: {ZIP_ARCH}")
    print(f"Archives gz: {GZ_ARCH}")
    print(f"Archives tar: {TAR_ARCH}")
    print(f"Documents doc: {DOC_DOCS}")
    print(f"Documents docx: {DOCX_DOCS}")
    print(f"Documents txt: {TXT_DOCS}")
    print(f"Documents pdf: {PDF_DOCS}")
    print(f"Documents xlsx: {XLSX_DOCS}")
    print(f"Documents pptx: {PPTX_DOCS}")
    print('*' * 25)
    print(f'Types of file in folder: {EXTENSIONS}')
    print(f'UNKNOWN: {UNKNOWN}')





