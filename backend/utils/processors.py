from models.brains import Brain
from models.files import File
from parsers.audio import process_audio
from parsers.csv import process_csv
from parsers.xlsx import process_xlsx
from parsers.docx import process_docx
from parsers.epub import process_epub
from parsers.html import process_html
from parsers.markdown import process_markdown
from parsers.notebook import process_ipnyb
from parsers.odt import process_odt
from parsers.pdf import process_pdf
from parsers.powerpoint import process_powerpoint
from parsers.txt import process_txt
from parsers.json import process_json
import shutil
from utils.file import convert_bytes
import pandas as pd
from bitarray import bitarray
import os
import sys

file_processors = {
    ".txt": process_txt,
    ".csv": process_csv,
    ".json": process_json,
    ".xlsx": process_xlsx,
    ".xls": process_xlsx,
    ".md": process_markdown,
    ".markdown": process_markdown,
    ".m4a": process_audio,
    ".mp3": process_audio,
    ".webm": process_audio,
    ".mp4": process_audio,
    ".mpga": process_audio,
    ".wav": process_audio,
    ".mpeg": process_audio,
    ".pdf": process_pdf,
    ".html": process_html,
    ".pptx": process_powerpoint,
    ".docx": process_docx,
    ".odt": process_odt,
    ".epub": process_epub,
    ".ipynb": process_ipnyb,
    ".sol": process_txt,
    ".jsx": process_txt,
}


def create_response(message, type):
    return {"message": message, "type": type}


async def filter_file(
    file: File,
    enable_summarization: bool,
    brain_id,
    openai_api_key,
):
    await file.compute_file_sha1()

    print("file sha1", file.file_sha1)
    file_exists = file.file_already_exists()
    file_exists_in_brain = file.file_already_exists_in_brain(brain_id)

    my_file_name = file.file_name
    if ".xlsx" in my_file_name:
        file_csv: File
        file_csv = file
        file_csv.file_name = "MY_CSV.csv"
        print ("----- FOUND XLSX fILE -----", file.file_name)
        print ("CWD for file = ", os.path.abspath(file.file_name), file.file_name)
        print ("This is inside processors.py and file_csv = ", file_csv.file_name)
        #print ("file_csv for file = ", os.path.abspath(file_csv.file_name), file_csv.file_name)

        # file_csv_content = file_csv.content
        # all_sheets = pd.read_excel(excel_file, sheet_name=None)
        # sheets = all_sheets.keys()

        # for sheet_name in sheets:
        #     sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
        #     sheet.to_csv("/tmp/%s.csv" % sheet_name, index=False)

        # Read the content of the original file
        #original_content = file.read()
        #original_xlsx_bins = file.content

        # excelFile = pd.read_excel('excelfile.xlsx', 'Sheet', index_col=None)
        # excelFile.to_csv ("ResultCsvFile.csv", index = None, header=True)

        original_xlsx_bins = file_csv.documents
        bts = bitarray()
        bts = bts.frombytes(original_xlsx_bins)
        
        print ("file_csv is type = ", type(file_csv))
        #ascs = bts.tobytes().decode('ascii')
        #converted_bytes = bts.tobytes()
        #xlsx = pd.read_excel(original_content) 

        #ascs = converted_bytes.decode('ascii')
        #ascs = original_xlsx_bins.decode('ascii')
        #ascs = ' '.join(str(c) for c in original_xlsx_bins)
        if bts is not None:
            ascs = bts.tobytes().decode('ascii')
                    # Create a new file to write the copied content
            new_file_path = "/tmp/"+"new_copy.txt"  # Change this to the desired path
            try:
                with open(new_file_path, "wb") as new_file:
                    new_file.write(ascs)
                    print (ascs)
                    #print ("-------ORGINAL CONTENT ---", original_content )
                    print("--------GOOD   File copied successfully!")
            except Exception as e:
                print("--------FAILED   File copied unsuccessfully!")
                print("Exception = ", e)
        # Perform further operations with 'ascs' if needed
        else:
            print("bts is None")


        #shutil.copyfile(file.file_name, '/tmp/TEMP.txt')
   

    if file_exists_in_brain:
        return create_response(
            f"🤔 {file.file.filename} already exists in brain {brain_id}.",  # pyright: ignore reportPrivateUsage=none
            "warning",
        )
    elif file.file_is_empty():
        return create_response(
            f"❌ {file.file.filename} is empty.",  # pyright: ignore reportPrivateUsage=none
            "error",  # pyright: ignore reportPrivateUsage=none
        )
    elif file_exists:
        file.link_file_to_brain(brain=Brain(id=brain_id))
        return create_response(
            f"✅ {file.file.filename} has been uploaded to brain {brain_id}.",  # pyright: ignore reportPrivateUsage=none
            "success",
        )


    if file.file_extension in file_processors:
        try:
            await file_processors[file.file_extension](
                file=file,
                enable_summarization=enable_summarization,
                brain_id=brain_id,
                user_openai_api_key=openai_api_key,
            )
            return create_response(
                f"✅ {file.file.filename} has been uploaded to brain {brain_id}.",  # pyright: ignore reportPrivateUsage=none
                "success",
            )
        except Exception as e:
            # Add more specific exceptions as needed.
            print(f"Error processing file: {e}")
            return create_response(
                f"⚠️ An error occurred while processing {file.file.filename}.",  # pyright: ignore reportPrivateUsage=none
                "error",
            )

    return create_response(
        f"❌ {file.file.filename} is not supported.",  # pyright: ignore reportPrivateUsage=none
        "error",
    )
