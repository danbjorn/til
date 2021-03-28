from pathlib import Path
from sqlite_utils import Database
import hashlib
import markdown
import yamldown


def build(paths, dbname, table):
    """
    Load markdown files into a SQLite database

    Based on https://github.com/simonw/markdown-to-sqlite, modified to use markdown
    extensions.
    """
    db = Database(dbname)
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite"],
        extension_configs={"codehilite": {"guess_lang": "False"}},
    )
    docs = []
    for path in paths:
        metadata, text = yamldown.load(open(path))
        html = md.convert(text)
        doc = {
            "_id": hashlib.sha1(str(path).encode("utf8")).hexdigest(),
            "_path": str(path),
            "text": text,
            "html": html,
            **(metadata or {}),
        }
        docs.append(doc)
    db[table].upsert_all(docs, pk="_id")


if __name__ == "__main__":
    build(Path("markdown").glob("*.md"), "til.db", "til")
