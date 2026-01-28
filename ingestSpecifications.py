import os
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.table import CT_Tbl


def tableToMarkdown(table):
    """Converts a python-docx table object to a Markdown string."""
    md_table = []
    # Handle potential empty tables or structural errors
    try:
        rows = table.rows
    except Exception:
        return ""
        
    if not rows:
        return ""
    for i, row in enumerate(rows):
        # Safety: str(cell.text or "") prevents NoneType errors if a cell is empty
        # .replace("|", "\\|") prevents internal pipes from breaking the MD columns
        cells = [str(cell.text or "").strip().replace("\n", "<br>").replace("|", "\\|") for cell in row.cells]
        
        md_row = f"| {' | '.join(cells)} |"
        md_table.append(md_row)
        
        # Markdown requirement: Separator row after the header (index 0)
        if i == 0:
            separator = f"| {' | '.join(['---'] * len(cells))} |"
            md_table.append(separator)        
    # Add double newlines to ensure the Markdown parser recognizes it as a block
    return "\n\n" + "\n".join(md_table) + "\n\n"

def convertSpecs(specPath):
    if not os.path.exists(specPath):
        print(f"Error: Path {specPath} not found.")
        return

    for filename in os.listdir(specPath):
        # 1. Standardize extension check & ignore temp files
        if filename.lower().endswith((".docx", ".doc")) and not filename.startswith("~$"):
            print(f"Converting {filename}...")
            
            # Normalize path for Windows/Linux consistency
            fullPath = os.path.normpath(os.path.abspath(os.path.join(specPath, filename)))         
            
            try:
                doc = Document(fullPath)
                mdLines = []     
                
                for block in doc.element.body.iterchildren():   
                    # PROCESS TABLES
                    if isinstance(block, CT_Tbl):
                        table = Table(block, doc)
                        mdLines.append(tableToMarkdown(table))
                        continue
                    
                    # PROCESS TEXT
                    if isinstance(block, Paragraph) or hasattr(block, 'text'):
                        para = Paragraph(block, doc) if not isinstance(block, Paragraph) else block
                        text = str(para.text or "").strip()
                        
                        # SKIP: Empty lines or Table of Contents entries
                        if not text or para.style.name.startswith('TOC'):
                            continue

                        # Heading Detection
                        if para.style.name.startswith('Heading 1'):
                            mdLines.append(f"# {text}")
                        elif para.style.name.startswith('Heading 2'):
                            mdLines.append(f"## {text}")
                        elif para.style.name.startswith('Heading 3'):
                            mdLines.append(f"### {text}")
                        else:
                            mdLines.append(text)
    
                finalText = "\n\n".join(mdLines)
                
                # 2. Robust filename generation
                baseName, _ = os.path.splitext(filename)
                newFileName = f"{baseName.lower()}.md"
                outputFile = os.path.join(specPath, newFileName)
                
                with open(outputFile, "w", encoding="utf-8") as f:
                    # Note: We keep the original filename in the header for source tracking
                    f.write(f"Source Document: {filename}\n\n{finalText}")
                
                print(f"Successfully Created: {newFileName}")             
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":  
    # Folder paths relative to LearnOneM2M root (acme md files will be saved here)
    acmePath = "rawData/implementations/acme"
    # (converted ts files to md will be saved here)
    specPath = "rawData/specifications"
    convertSpecs(specPath)