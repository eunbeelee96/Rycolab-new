#!/usr/bin/env python3
"""
add_topics_to_publications.py

Reads topic_keywords.json and injects a `topics:` field into the YAML
frontmatter of each matching publication's index.md.

Cite-key → Hugo-slug transformation:
  amini+al.acl23       → aminial-acl-23
  cotterell+al.naacl18a → cotterellal-naacl-18-a
  du+al2.acl24          → dual-2-acl-24
  hall-maudslay+al.emnlp-ijcnlp19 → hall-maudslayal-emnlp-ijcnlp-19
"""
import json
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JSON_PATH = os.path.join(BASE, "data", "topic_keywords.json")
PUBS_DIR  = os.path.join(BASE, "content", "publications")


def cite_key_to_slug(key: str) -> str:
    """Convert a bibtex-style cite key to a Hugo directory slug."""
    if "." in key:
        dot_idx = key.index(".")
        author_raw = key[:dot_idx]
        venue_year = key[dot_idx + 1:]
        author = author_raw.replace("+", "")
    else:
        author = key.replace("+", "")
        venue_year = ""

    # Replace any remaining dots in venue_year (e.g. "acl.16") with hyphens
    venue_year = venue_year.replace(".", "-")

    # Insert hyphen between letter and digit (both directions) in author
    author = re.sub(r"([A-Za-z])(\d)", r"\1-\2", author)
    author = re.sub(r"(\d)([A-Za-z])", r"\1-\2", author)

    if venue_year:
        venue_year = re.sub(r"([A-Za-z])(\d)", r"\1-\2", venue_year)
        venue_year = re.sub(r"(\d)([A-Za-z])", r"\1-\2", venue_year)
        slug = f"{author}-{venue_year}"
    else:
        slug = author

    return slug.lower()


def patch_frontmatter(path: str, topics: list[str]) -> bool:
    """Add/update `topics:` in the YAML frontmatter of a file. Returns True if changed."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        print(f"  SKIP (no frontmatter): {path}")
        return False

    # Find the closing --- that is on its OWN LINE (not inside a YAML value)
    m = re.search(r'^---\s*$', content[3:], flags=re.MULTILINE)
    if not m:
        print(f"  SKIP (no closing ---): {path}")
        return False
    end = 3 + m.start()   # position of the closing ---

    front = content[3:end]  # content between opening and closing ---
    rest  = content[end:]   # closing --- and body

    # Build topics YAML block
    topics_yaml = "topics:\n" + "".join(f"- '{t}'\n" for t in topics)

    # Remove existing topics block if present
    front = re.sub(r"^topics:.*?(?=\n[a-z_]|\n---|\Z)", "", front, flags=re.M | re.S)
    front = front.rstrip("\n") + "\n" + topics_yaml

    new_content = "---" + front + rest
    if new_content == content:
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # slug → topics (last write wins for duplicate slugs with same topics)
    slug_to_topics: dict[str, list[str]] = {}
    for key, topics in data.items():
        slug = cite_key_to_slug(key)
        slug_to_topics[slug] = topics

    # Print a few for sanity check
    print("=== Sample slug transformations ===")
    samples = ["amini+al.acl23", "cotterell+al.naacl18a", "du+al2.acl24",
               "hall-maudslay+al.emnlp-ijcnlp19", "meister+al.acl2021a",
               "pimentel2+al.emnlp20", "opedal+acl23"]
    for s in samples:
        if s in data:
            print(f"  {s} → {cite_key_to_slug(s)}")

    print(f"\nProcessing {len(slug_to_topics)} unique slugs across {len(data)} JSON entries...")

    matched = 0
    unmatched = []

    for slug, topics in slug_to_topics.items():
        pub_dir  = os.path.join(PUBS_DIR, slug)
        md_path  = os.path.join(pub_dir, "index.md")
        if not os.path.isfile(md_path):
            unmatched.append(slug)
            continue
        changed = patch_frontmatter(md_path, topics)
        if changed:
            matched += 1

    print(f"\n✓ Updated {matched} publications.")
    if unmatched:
        print(f"\n! No directory found for {len(unmatched)} slug(s):")
        for u in sorted(unmatched):
            print(f"  {u}")


if __name__ == "__main__":
    main()
