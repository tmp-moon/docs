from python_notion_exporter import NotionExporter, ExportType, ViewExportType
import os

github_token = os.getenv("GITHUB_TOKEN")
notion_token = os.getenv("NOTION_TOKEN")
notion_file_token = os.getenv("NOTION_FILE_TOKEN")
page = os.getenv("NOTION_PAGE", "111a77bf59b480d9b0ebfe5b3743e768")

if __name__ == "__main__":
    exporter = NotionExporter(
        token_v2=notion_token,
        file_token=notion_file_token,
        pages={"Documentation": page},
        export_directory=".notion-exporter",
        export_name="export",
        flatten_export_file_tree=True,
        export_type=ExportType.MARKDOWN,
        current_view_export_type=ViewExportType.CURRENT_VIEW,
        include_files=True,
        recursive=True
    )
    exporter.process()