import sqlite3
DB=".governance/registry.db"
SCHEMA=1
TABLES=("files" "edges" "audit_log" "scan_runs" "issues" "schema_meta")
def connect():
 c=sqlite3.connect(DB)
 c.execute("PRAGMA foreign_keys=ON")
 return c
FILES_SQL="""CREATE TABLE IF NOT EXISTS files(
file_id TEXT PRIMARY KEY,
rel_path TEXT UNIQUE NOT NULL,
domain TEXT NOT NULL,
content_hash TEXT,
ast_hash TEXT,
git_blob TEXT,
mtime_ns INTEGER,
size_bytes INTEGER,
last_verified TEXT,
created_at TEXT NOT NULL
);"""
EDGES_SQL="""CREATE TABLE IF NOT EXISTS edges(
src_file_id TEXT NOT NULL,
dst_file_id TEXT,
import_name TEXT NOT NULL,
resolved INTEGER NOT NULL DEFAULT 0,
PRIMARY KEY(src_file_id,import_name))";
